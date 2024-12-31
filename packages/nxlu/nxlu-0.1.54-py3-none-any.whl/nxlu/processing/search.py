import gc
import hashlib
import json
import logging
import warnings
from collections import defaultdict
from pathlib import Path
from typing import Any

import faiss
import networkx as nx
import numpy as np
from sentence_transformers.quantization import (
    quantize_embeddings,
    semantic_search_faiss,
)

from nxlu.config import Precision
from nxlu.processing.community import ConsensusResult, get_communities
from nxlu.processing.embed import SentenceTransformerEmbedding

warnings.filterwarnings("ignore")

logger = logging.getLogger("nxlu")

__all__ = [
    "SemanticSearchEmbedding",
    "QueryCommunityMembers",
    "CommunityQueryMatcher",
]

faiss.omp_set_num_threads(1)

EDGE_ID_SEPARATOR = "||"


class SemanticSearchEmbedding(SentenceTransformerEmbedding):
    """Extends SentenceTransformerEmbedding with FAISS-based semantic search
    capabilities.
    """

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
        batch_size: int = 32,
        cache_dir: str = str(Path.home() / "nxlu_cache"),
        precision: Precision = Precision.FLOAT32,
    ):
        super().__init__(model_name, batch_size, cache_dir, precision)

    def build_faiss_index(
        self,
        texts: list[str],
        similarity_metric: str = "cosine",
        precision: Precision | None = None,
    ) -> faiss.Index:
        """Build a FAISS index from a list of texts."""
        embeddings = self.get_text_embeddings(texts)
        precision = precision or self.precision
        embeddings = quantize_embeddings(embeddings, precision=precision.value)
        if similarity_metric == "cosine":
            embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        index = self._initialize_faiss_index(similarity_metric)
        index.add(embeddings)
        return index

    def load_faiss_index(self, index_path: str) -> faiss.Index:
        """Load a FAISS index from a file."""
        index = faiss.read_index(index_path)
        return index

    def search_faiss(
        self,
        query: str,
        index: faiss.Index,
        top_k: int = 10,
        similarity_metric: str = "cosine",
        precision: Precision | None = None,
    ) -> list[dict]:
        """Perform semantic search using FAISS."""
        query_embedding = self.get_query_embedding(query)
        precision = precision or self.precision
        query_embedding = quantize_embeddings(
            query_embedding, precision=precision.value
        )
        if similarity_metric == "cosine":
            query_embedding = query_embedding / np.linalg.norm(
                query_embedding, axis=1, keepdims=True
            )
        results = semantic_search_faiss(
            query_embeddings=query_embedding,
            corpus_index=index,
            top_k=top_k,
            corpus_precision=precision.value,
            rescore=False,
            output_index=False,
            exact=False,
        )[0][0]
        return results

    def _initialize_faiss_index(self, similarity_metric: str) -> faiss.Index:
        """Initialize a FAISS index based on the similarity metric."""
        dim = self.model.get_sentence_embedding_dimension()
        if similarity_metric == "cosine":
            index = faiss.IndexFlatIP(dim)
        elif similarity_metric == "euclidean":
            index = faiss.IndexFlatL2(dim)
        else:
            raise ValueError(f"Unsupported similarity metric: {similarity_metric}")
        return index


class QueryCommunityMembers:
    """Query for most semantically relevant nodes and edges within detected communities.

    This class uses FAISS to efficiently search for nodes and edges that are most
    semantically similar to a query within each community. It maintains separate indices
    for nodes and edges, with caching for performance.

    Parameters
    ----------
    embedding_model : SemanticSearchEmbedding
        An instance of SemanticSearchEmbedding to be used for embedding and semantic
        search.
    similarity_metric : str
        The similarity metric used for querying ('cosine' or 'euclidean').
    include_edges : bool
        Whether to also index and query edges.
    cache_dir : str
        Directory for caching FAISS indices.
    """

    def __init__(
        self,
        embedding_model: SemanticSearchEmbedding,
        similarity_metric: str = "cosine",
        include_edges: bool = False,
        cache_dir: str = str(Path.home() / ".nxlu_cache"),
    ):
        self.embedding_model = embedding_model
        self.similarity_metric = similarity_metric
        self.cache_dir = Path(cache_dir)
        self.include_edges = include_edges

        self.precision = self.embedding_model.precision
        self.dim = self.embedding_model.model.get_sentence_embedding_dimension()

        self.consensus: ConsensusResult | None = None
        self.community_node_indices: dict[tuple[int, str], faiss.Index] = {}
        self.community_edge_indices: dict[tuple[int, str], faiss.Index] = {}

        self.node_id_maps: dict[tuple[int, str], dict[int, str]] = {}
        self.edge_id_maps: dict[tuple[int, str], dict[int, str]] = {}

        self.node_text_maps: dict[tuple[int, str], list[str]] = {}
        self.edge_text_maps: dict[tuple[int, str], list[str]] = {}

        self.node_similarity_scores: dict[tuple[int, str], dict[str, float]] = (
            defaultdict(dict)
        )

    def prepare_community_indices(
        self,
        graph: nx.Graph,
        consensus: ConsensusResult,
        similar_communities: list[tuple[tuple[int, str], float]],
    ) -> None:
        """Prepare FAISS indices for the similar communities.

        Parameters
        ----------
        graph : nx.Graph
            The full graph
        consensus : ConsensusResult
            Community detection results
        similar_communities : List[Tuple[Tuple[int, str], float]]
            List of (community_id, similarity) pairs
        """
        self.consensus = consensus
        self.graph = graph

        for community_id, _similarity in similar_communities:
            level_idx, comm_name = community_id
            community_nodes = self.consensus.hierarchical_levels[level_idx][
                int(comm_name.split("_")[1])
            ]

            # get the community subgraph
            community_graph = graph.subgraph(community_nodes).copy()

            self._prepare_node_index(community_id, community_graph)

            if self.include_edges:
                self._prepare_edge_index(community_id, community_graph)

    def _prepare_node_index(
        self,
        community_id: tuple[int, str],
        community_graph: nx.Graph,
    ) -> None:
        """Prepare FAISS index for nodes in a community."""
        nodes_data = [
            (str(node), data) for node, data in community_graph.nodes(data=True)
        ]

        if not nodes_data:
            logger.warning(f"No nodes to index in community {community_id}")
            return

        texts = [
            f"Node: {node_id}, Attributes: {data}, Description: "
            f"{data.get('description', '')}"
            for node_id, data in nodes_data
        ]

        self.node_text_maps[community_id] = texts

        node_checksum = self._compute_checksum(
            texts, f"nodes_{community_id[0]}_{community_id[1]}"
        )
        index_name = f"nodes_index_{node_checksum}"
        index_path = self.cache_dir / f"{index_name}.faiss"

        if index_path.exists():
            logger.debug(f"Using existing node embedding indices: {index_path}")
            index = self.embedding_model.load_faiss_index(str(index_path))
            self.community_node_indices[community_id] = index

            id_map_path = index_path.with_suffix(".json")
            if id_map_path.exists():
                with id_map_path.open() as f:
                    self.node_id_maps[community_id] = json.load(f)
        else:
            index = self.embedding_model.build_faiss_index(
                texts=texts,
                similarity_metric=self.similarity_metric,
            )
            self.community_node_indices[community_id] = index

            faiss.write_index(index, str(index_path))

            self.node_id_maps[community_id] = {
                idx: node_id for idx, (node_id, _) in enumerate(nodes_data)
            }
            with (self.cache_dir / f"{index_name}.json").open("w") as f:
                json.dump(self.node_id_maps[community_id], f)

    def _prepare_edge_index(
        self,
        community_id: tuple[int, str],
        community_graph: nx.Graph,
    ) -> None:
        """Prepare FAISS index for edges in a community."""
        edge_data = []
        edge_ids = []

        if isinstance(community_graph, (nx.MultiGraph, nx.MultiDiGraph)):
            for u, v, key, data in community_graph.edges(keys=True, data=True):
                edge_id = f"{u}{EDGE_ID_SEPARATOR}{v}{EDGE_ID_SEPARATOR}{key}"
                edge_data.append((u, v, key, data, edge_id))
        else:
            for u, v, data in community_graph.edges(data=True):
                edge_id = f"{u}{EDGE_ID_SEPARATOR}{v}"
                edge_data.append((u, v, data, edge_id))

        if not edge_data:
            logger.warning(f"No edges to index in community {community_id}")
            return

        texts = []
        for entry in edge_data:
            if isinstance(community_graph, (nx.MultiGraph, nx.MultiDiGraph)):
                u, v, key, data, edge_id = entry
            else:
                u, v, data, edge_id = entry

            text = (
                f"Edge: {u} -- {data.get('relation', 'EDGE')} "
                f"(Weight: {data.get('weight', 'N/A')}) "
                f"--> {v} | ID: {edge_id}"
            )
            texts.append(text)
            edge_ids.append(edge_id)

        self.edge_text_maps[community_id] = texts

        edge_checksum = self._compute_checksum(
            texts, f"edges_{community_id[0]}_{community_id[1]}"
        )
        index_name = f"edges_index_{edge_checksum}"
        index_path = self.cache_dir / f"{index_name}.faiss"

        if index_path.exists():
            logger.debug(f"Using existing edge embedding indices: {index_path}")
            index = self.embedding_model.load_faiss_index(str(index_path))
            self.community_edge_indices[community_id] = index

            id_map_path = index_path.with_suffix(".json")
            if id_map_path.exists():
                with id_map_path.open() as f:
                    self.edge_id_maps[community_id] = json.load(f)
        else:
            index = self.embedding_model.build_faiss_index(
                texts=texts,
                similarity_metric=self.similarity_metric,
            )
            self.community_edge_indices[community_id] = index

            faiss.write_index(index, str(index_path))

            self.edge_id_maps[community_id] = dict(enumerate(edge_ids))
            with (self.cache_dir / f"{index_name}.json").open("w") as f:
                json.dump(self.edge_id_maps[community_id], f)

    def query_communities(
        self,
        query: str,
        top_k_nodes: int = 500,
        top_k_edges: int = 1000,
    ) -> tuple[
        dict[tuple[int, str], list[str]], dict[tuple[int, str], list[tuple[str, ...]]]
    ]:
        """Query each community for relevant nodes and edges."""
        if not self.consensus:
            raise ValueError("Must call prepare_community_indices() before querying")

        community_nodes = {}
        community_edges = {}

        for community_id in self.community_node_indices:
            index = self.community_node_indices[community_id]

            logger.debug(f"\nProcessing community {community_id}")
            logger.debug(f"Node index contains {index.ntotal} vectors")

            if community_id in self.node_id_maps:
                logger.debug(f"Node text examples for community {community_id}:")
                if community_id in self.node_text_maps:
                    for i, text in enumerate(self.node_text_maps[community_id][:3]):
                        logger.debug(f"Node {i}: {text}")

                node_results = self.embedding_model.search_faiss(
                    query=query,
                    index=index,
                    top_k=min(top_k_nodes, index.ntotal),
                    similarity_metric=self.similarity_metric,
                )

                logger.debug(f"Retrieved {len(node_results)} results from FAISS")

                node_ids = []
                similarity_scores = []

                self.node_similarity_scores[community_id] = {}

                for hit in node_results:
                    corpus_id = int(hit["corpus_id"])
                    score = float(hit["score"])

                    logger.debug(f"Hit - corpus_id: {corpus_id}, score: {score}")

                    node_id = self.node_id_maps[community_id].get(
                        str(corpus_id)
                    ) or self.node_id_maps[community_id].get(corpus_id)

                    if node_id:
                        logger.debug(f"Found node_id: {node_id} with score: {score}")
                        node_ids.append(node_id)
                        similarity_scores.append(score)
                        self.node_similarity_scores[community_id][node_id] = score
                    else:
                        logger.warning(f"No node ID found for corpus_id {corpus_id}")

                if node_ids:
                    logger.info(
                        f"Community {community_id}: Found {len(node_ids)} relevant "
                        f"nodes with scores from {min(similarity_scores):.3f} to "
                        f"{max(similarity_scores):.3f}"
                    )
                    community_nodes[community_id] = node_ids
                else:
                    logger.warning(
                        f"No nodes above threshold found for community {community_id}"
                    )

        if self.include_edges:
            for community_id in self.community_edge_indices:
                index = self.community_edge_indices[community_id]

                logger.debug(f"Edge index contains {index.ntotal} vectors")

                edge_results = self.embedding_model.search_faiss(
                    query=query,
                    index=index,
                    top_k=min(top_k_edges, index.ntotal),
                    similarity_metric=self.similarity_metric,
                )

                edge_tuples = []
                for hit in edge_results:
                    corpus_id = int(hit["corpus_id"])
                    edge_id = self.edge_id_maps[community_id].get(str(corpus_id))
                    if edge_id is None:
                        edge_id = self.edge_id_maps[community_id].get(corpus_id)

                    if edge_id:
                        edge_tuple = tuple(edge_id.split(EDGE_ID_SEPARATOR))
                        if self._validate_edge_tuple(edge_tuple):
                            edge_tuples.append(edge_tuple)

                if edge_tuples:
                    community_edges[community_id] = edge_tuples

        logger.debug(f"Total communities with nodes: {len(community_nodes)}")
        logger.debug(f"Total communities with edges: {len(community_edges)}")

        return community_nodes, community_edges

    def create_query_subgraph(
        self,
        query: str,
        similar_communities: list[tuple[tuple[int, str], float]],
    ) -> dict[tuple[int, str], dict[str, Any]]:
        """Return dictionary of similar communities mapped to their subgraphs, nodes
        and edges.

        Parameters
        ----------
        query : str
            The query string
        similar_communities : List[Tuple[Tuple[int, str], float]]
            List of (community_id, similarity) pairs from CommunityQueryMatcher

        Returns
        -------
        Dict[Tuple[int, str], Dict[str, Any]]
            Dictionary mapping community IDs to:
                - subgraph: nx.Graph of the community
                - nodes: List of most similar nodes
                - edges: List of most similar edges
                - similarity_scores: Dict mapping nodes to their similarity scores
        """
        community_nodes, community_edges = self.query_communities(query)

        relevance_dict = {}

        for community_id, _similarity in similar_communities:
            level_idx, comm_name = community_id
            community_nodes_set = self.consensus.hierarchical_levels[level_idx][
                int(comm_name.split("_")[1])
            ]

            community_subgraph = self.graph.subgraph(community_nodes_set).copy()
            relevance_dict[community_id] = {
                "subgraph": community_subgraph,
                "nodes": [],
                "edges": [],
                "similarity_scores": {},
            }

            if (
                community_id in community_nodes
                and community_id in self.node_similarity_scores
            ):
                nodes = community_nodes[community_id]
                scores = self.node_similarity_scores[community_id]

                for node in nodes:
                    score = scores.get(node, 0)
                    relevance_dict[community_id]["nodes"].append(node)
                    relevance_dict[community_id]["similarity_scores"][node] = score

            if self.include_edges and community_id in community_edges:
                edges = community_edges[community_id]
                if isinstance(self.graph, (nx.MultiGraph, nx.MultiDiGraph)):
                    edges = [
                        (u, v, k)
                        for (u, v, k) in edges
                        if self.graph.has_edge(u, v, key=k)
                    ]
                else:
                    edges = [(u, v) for (u, v) in edges if self.graph.has_edge(u, v)]
                relevance_dict[community_id]["edges"] = edges

        logger.info(
            f"Found relevant nodes/edges across {len(relevance_dict)} communities for "
            f"query: '{query}'"
        )

        for community_id, data in relevance_dict.items():
            logger.debug(
                f"Community {community_id}: "
                f"subgraph size: {data['subgraph'].number_of_nodes()} nodes "
                f"and {data['subgraph'].number_of_edges()} edges, "
                f"similar nodes: {len(data['nodes'])}, "
                f"similar scores: {len(data['similarity_scores'])}, "
                f"similar edges: {len(data['edges'])}"
            )

        return relevance_dict

    def _compute_checksum(self, texts: list[str], index_type: str) -> str:
        """Compute SHA256 checksum based on texts and embedding parameters."""
        try:
            data = {
                "index_type": index_type,
                "similarity_metric": self.similarity_metric,
                "embedding_model_name": self.embedding_model.model_name,
                "precision": self.precision.name,
                "texts": texts,
            }
            data_bytes = json.dumps(data, sort_keys=True).encode("utf-8")
        except Exception as e:
            logger.exception("Failed to compute checksum.")
            raise
        return hashlib.sha256(data_bytes).hexdigest()

    def _validate_edge_tuple(self, edge_tuple: tuple[str, ...]) -> bool:
        """Validate the edge tuple based on the graph type."""
        if isinstance(self.graph, (nx.MultiGraph, nx.MultiDiGraph)):
            return len(edge_tuple) == 3 and self.graph.has_edge(
                edge_tuple[0], edge_tuple[1], key=edge_tuple[2]
            )
        return len(edge_tuple) == 2 and self.graph.has_edge(
            edge_tuple[0], edge_tuple[1]
        )

    def cleanup(self):
        """Clean up resources."""
        logger.info("Cleaning up FAISS indices.")
        if hasattr(self, "community_node_indices"):
            for key in list(self.community_node_indices.keys()):
                del self.community_node_indices[key]
        if hasattr(self, "community_edge_indices"):
            for key in list(self.community_edge_indices.keys()):
                del self.community_edge_indices[key]
        gc.collect()

    def __del__(self):
        try:
            self.cleanup()
        except Exception as e:
            logger.exception("Exception during cleanup in __del__.")


class CommunityQueryMatcher:
    """Match queries to detected graph communities using semantic similarity.

    This class performs multi-resolution community detection on a graph and identifies
    the most semantically similar communities to a given query.

    Parameters
    ----------
    embedding_model : SemanticSearchEmbedding
        An instance of SemanticSearchEmbedding to be used for embedding and semantic
        search.

    Attributes
    ----------
    embedding_model : SemanticSearchEmbedding
        Model for computing text embeddings and performing semantic search.
    consensus : ConsensusResult
        Consensus community detection result.
    community_descriptions : List[str]
        Textual descriptions of each community.
    community_ids : List[Tuple[int, str]]
        List of community identifiers corresponding to descriptions.
    faiss_index : faiss.Index
        FAISS index built over community embeddings.
    """

    def __init__(self, embedding_model: SemanticSearchEmbedding):
        self.embedding_model = embedding_model
        self.consensus: ConsensusResult | None = None
        self.community_descriptions: list[str] = []
        self.community_ids: list[tuple[int, str]] = []
        self.faiss_index: faiss.Index | None = None

    def fit(self, graph: nx.Graph) -> None:
        """Detect communities and compute their embeddings.

        Parameters
        ----------
        graph : nx.Graph
            Input graph to analyze.
        """
        self.consensus = get_communities(graph)

        self.community_descriptions = []
        self.community_ids = []

        for level_idx, level_communities in enumerate(
            self.consensus.hierarchical_levels
        ):
            for community_idx, community in enumerate(level_communities):
                desc = self._get_community_description(graph, community)
                self.community_descriptions.append(desc)
                self.community_ids.append((level_idx, f"community_{community_idx}"))

        self.faiss_index = self.embedding_model.build_faiss_index(
            texts=self.community_descriptions
        )

    def _get_community_description(self, graph: nx.Graph, nodes: set[Any]) -> str:
        """Generate a text description of a community from node attributes.

        Parameters
        ----------
        graph : nx.Graph
            The input graph.
        nodes : Set[Any]
            Set of node IDs in the community.

        Returns
        -------
        str
            Text description of the community.
        """
        descriptions = []
        for node in nodes:
            node_data = graph.nodes[node]
            desc_parts = []

            if "label" in node_data:
                desc_parts.append(str(node_data["label"]))
            if "description" in node_data:
                desc_parts.append(str(node_data["description"]))
            if "type" in node_data:
                desc_parts.append(f"Type: {node_data['type']}")

            if desc_parts:
                descriptions.append(" ".join(desc_parts))

        if descriptions:
            return " ".join(descriptions)
        return " ".join(map(str, nodes))

    def transform(
        self, query: str, n_communities: int = 10, min_similarity: float = 0.2
    ) -> list[tuple[tuple[int, str], float]]:
        """Find the most semantically similar communities to a query.

        Parameters
        ----------
        query : str
            Input query text.
        n_communities : int
            Maximum number of communities to return.
        min_similarity : float
            Minimum cosine similarity threshold.

        Returns
        -------
        List[Tuple[Tuple[int, str], float]]
            List of (community_id, similarity_score) pairs, sorted by similarity.
        """
        if self.faiss_index is None:
            raise ValueError("Must call fit() before finding similar communities")

        results = self.embedding_model.search_faiss(
            query=query,
            index=self.faiss_index,
            top_k=n_communities,
            similarity_metric="cosine",
        )

        similarities = []
        for hit in results:
            corpus_id = int(hit["corpus_id"])
            score = float(hit["score"])
            if score >= min_similarity:
                comm_id = self.community_ids[corpus_id]
                similarities.append((comm_id, score))

        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:n_communities]

    def get_community_nodes(self, community_id: tuple[int, str]) -> set[Any]:
        """Get the nodes belonging to a community.

        Parameters
        ----------
        community_id : Tuple[int, str]
            The (level, community_id) identifier.

        Returns
        -------
        Set[Any]
            Set of node IDs in the community.
        """
        if not self.consensus or not self.consensus.hierarchical_levels:
            raise ValueError("Must call fit() before getting community nodes")

        level_idx, comm_id = community_id
        community_idx = int(comm_id.split("_")[1])
        return self.consensus.hierarchical_levels[level_idx][community_idx]
