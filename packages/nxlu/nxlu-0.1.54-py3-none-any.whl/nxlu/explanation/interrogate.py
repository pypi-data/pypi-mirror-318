import asyncio
import logging
import warnings

import networkx as nx

from nxlu.config import Intent, NxluConfig
from nxlu.explanation.entities import EntityExtractor
from nxlu.io import load_algorithm_docs, load_algorithm_encyclopedia
from nxlu.processing.analyze import GraphProperties, analyze_relationships
from nxlu.processing.optimize import (
    AlgorithmElector,
    AlgorithmNominator,
    GraphPreprocessingSelector,
)
from nxlu.processing.preprocess import CleanGraph
from nxlu.processing.search import (
    CommunityQueryMatcher,
    QueryCommunityMembers,
    SemanticSearchEmbedding,
)
from nxlu.processing.subgraph import QuerySubgraphHandler
from nxlu.processing.summarize import characterize_graph, format_algorithm_results
from nxlu.utils.control import ResourceManager
from nxlu.utils.misc import scrub_braces

warnings.filterwarnings("ignore")


logger = logging.getLogger("nxlu")

__all__ = ["GraphInterrogator"]


class GraphInterrogator:
    """A class to interrogate and analyze NetworkX graphs using integrated algorithms
    and language models.

    Attributes
    ----------
    config : NxluConfig
        Configuration settings for the model.
    llm : Any
        Initialized language model.
    classifier : Any
        Zero-shot classification pipeline.
    algorithm_applicability : Dict[str, Dict[str, Any]]
        Dictionary mapping algorithms to their applicability conditions.
    applicable_algorithms : List[str]
        List of algorithms applicable to the graph.
    preprocessing_config : Any
        Configuration for graph preprocessing.
    graph_summary : str
        Summary of the graph.
    selected_algorithms : List[str]
        Algorithms selected based on classification.
    results : Dict[str, Any]
        Results from applied algorithms.
    """

    def __init__(self, config: NxluConfig):
        """Initialize the GraphInterrogator with necessary models and classifiers.

        Parameters
        ----------
        config : NxluConfig
            Configuration settings for the model.
        backend : BaseBackend
            The backend instance to use for running algorithms.
        """
        self.config = config
        self.algorithm_applicability = load_algorithm_encyclopedia()
        self.algorithm_docs = load_algorithm_docs()
        self.entity_extractor = EntityExtractor()
        self.resource_manager = ResourceManager()

    async def reason_async(
        self,
        graph: nx.Graph,
        query: str | None = None,
        intent: list[Intent] | None = None,
    ) -> str:
        """Asynchronously generate reasoning based on the graph and query.

        Parameters
        ----------
        graph : nx.Graph
            The NetworkX graph to analyze.
        query : str
            The user's query.
        intent : List[Intent]
            Inferred high-level intents from user queries. Default is exploration.

        Returns
        -------
        str
            The reasoning result.
        """
        if intent is None:
            intent = [Intent.EXPLORATION]
        loop = asyncio.get_event_loop()
        graph_info = await loop.run_in_executor(None, self.reason, graph, query, intent)
        return graph_info

    def reason(
        self,
        graph: nx.Graph,
        query: str | None = None,
        intent: list[Intent] | None = None,
    ) -> dict | str:
        """Generate reasoning based on the graph and query.

        Parameters
        ----------
        graph : nx.Graph
            The NetworkX graph to analyze. If None, generate a simple response.
        query : str
            The user's query.
        intent : List[Intent]
            Inferred high-level intents from user queries. Default is exploration.

        Returns
        -------
        str
            The reasoning result.
        """
        if intent is None:
            intent = [Intent.EXPLORATION]

        graph_props = GraphProperties(graph)

        if (
            query
            and self.config.enable_subgraph_retrieval
            and graph_props.has_user_node_data
        ):
            self.sse = SemanticSearchEmbedding(
                model_name=self.config.embedding_model_name
            )
            self.query_matcher = CommunityQueryMatcher(embedding_model=self.sse)
            self.query_matcher.fit(graph_props.graph)
            similar_communities = self.query_matcher.transform(query)
            self.community_querier = QueryCommunityMembers(embedding_model=self.sse)

            try:
                self.community_querier.prepare_community_indices(
                    graph_props.graph,
                    self.query_matcher.consensus,
                    similar_communities,
                )
                relevance_dict = self.community_querier.create_query_subgraph(
                    query, similar_communities
                )
                sg_handler = QuerySubgraphHandler(relevance_dict)
                subgraph = sg_handler.get_relevant_subgraph()
            finally:
                self.community_querier.cleanup()
        else:
            logger.info(
                "Nodes lack attributes or subgraph retrieval disabled. Proceeding "
                "without similarity search."
            )
            self.config.set_enable_subgraph_retrieval(False)
            subgraph = graph_props.graph

        if subgraph.number_of_nodes() == 0:
            error_msg = "Subgraph is empty after querying. Search failed."
            logger.error(error_msg)
            return error_msg

        graph_props = GraphProperties(subgraph)

        with AlgorithmNominator(
            applicability_dict=self.algorithm_applicability,
            resource_manager=self.resource_manager,
            include_algorithms=self.config.include_algorithms,
            exclude_algorithms=self.config.exclude_algorithms,
            enable_classification=self.config.enable_classification,
            enable_resource_constraints=self.config.enable_resource_constraints,
        ) as nominator:
            applicable_algorithms = nominator.select_algorithms(
                graph_props, query, intent
            )

        if not applicable_algorithms:
            return "No applicable algorithms found for the given graph."

        preprocessing_classifier = GraphPreprocessingSelector(
            self.algorithm_applicability
        )
        preprocessing_config = preprocessing_classifier.select_preprocessing_steps(
            subgraph, applicable_algorithms
        )

        cleaner = CleanGraph(subgraph, preprocessing_config)
        clean_subgraph = cleaner.clean()

        try:
            clean_props = GraphProperties(clean_subgraph)
            (
                clean_subgraph,
                graph_summary,
                relevant_authorities,
                relevant_hubs,
            ) = characterize_graph(
                graph_props=clean_props,
                user_query=query,
                detect_domain=True,
            )
        except Exception:
            logger.exception("Error characterizing graph. Using minimal summary.")
            graph_summary = f"Graph with {clean_subgraph.number_of_nodes()} nodes and "
            f"{clean_subgraph.number_of_edges()} edges."
            relevant_authorities, relevant_hubs = [], []

        if not query:
            important_nodes = list(
                {str(n) for n in relevant_hubs} | {str(n) for n in relevant_authorities}
            )
        else:
            important_nodes = []

        with AlgorithmElector(
            algorithm_docs=self.algorithm_docs,
            applicability_dict=self.algorithm_applicability,
            include_algorithms=self.config.include_algorithms,
            exclude_algorithms=self.config.exclude_algorithms,
            enable_classification=self.config.enable_classification,
        ) as classifier:
            elected_algorithms = classifier.elect_algorithms(
                query=query,
                graph_summary=graph_summary,
                user_intent=intent,
                candidates=applicable_algorithms,
            )
            results = classifier.apply_elected_algorithms(
                graph=clean_subgraph,
                algorithms=elected_algorithms,
                query=query,
                user_intent=intent,
            )

        consolidated_results = list(results.items())
        formatted_results = format_algorithm_results(consolidated_results)

        if query:
            query_entities = self.entity_extractor.extract_all_entities(query)
            logger.info(f"Named entities extracted: {query_entities}")
            relevant_nodes = [
                n
                for n, _ in clean_subgraph.nodes(data=True)
                if any(str(n).lower() == e.lower() for e in query_entities)
            ]
            logger.info(f"Relevant Nodes: {relevant_nodes}")
            important_nodes.extend(relevant_nodes)

        if len(important_nodes) > 0:
            nodes_to_include = set()
            for node in important_nodes:
                node = int(node) if str(node).isnumeric() else node
                nodes_to_include.add(node)
                neighbors = list(subgraph.neighbors(node))
                nodes_to_include.update(neighbors)
            important_subgraph = subgraph.subgraph(nodes_to_include)

            node_pairs = [
                (important_nodes[i], important_nodes[j])
                for i in range(len(important_nodes))
                for j in range(i + 1, len(important_nodes))
            ]

            subgraph_relationships = analyze_relationships(
                important_subgraph, node_pairs
            )
            subgraph_relationships = (
                f"Named entities, hubs, and/or authorities = "
                f"{important_subgraph.nodes(data=True)}\n\n" + subgraph_relationships
            )
        else:
            subgraph_relationships = "No named entity nodes, hubs, or authorities "
            "identified"

        compiled_results = {
            "Graph Summary": graph_summary,
            "Descriptions of Applied Algorithms": dict(
                zip(
                    elected_algorithms,
                    [self.algorithm_docs[alg] for alg in elected_algorithms],
                )
            ),
            "Graph Analysis": formatted_results,
            "Important Nodes and their Relationships": subgraph_relationships,
        }

        return scrub_braces(compiled_results)
