import logging
import re
import warnings
from threading import Lock
from typing import Any

import networkx as nx
from transformers import pipeline

from nxlu.config import COMPLEXITY_COST_MAPPING, Intent, PathIntent, RescalingMethod
from nxlu.constants import PathConcepts
from nxlu.explanation.entities import EntityExtractor
from nxlu.processing.analyze import (
    GraphProperties,
    apply_algorithm,
    map_algorithm_result,
)
from nxlu.processing.paths import PathQueryAnalyzer, filter_path_algorithms
from nxlu.processing.preprocess import (
    CleanGraphConfig,
    GraphRescalingConfig,
    GraphThresholdingConfig,
    SubgraphSelectionConfig,
    get_connected_components,
)
from nxlu.utils.control import ResourceManager

warnings.filterwarnings("ignore")


logger = logging.getLogger("nxlu")


__all__ = [
    "AlgorithmNominator",
    "AlgorithmElector",
    "GraphPreprocessingSelector",
    "apply_algorithm",
    "map_algorithm_result",
    "GraphProperties",
    "GraphRescalingConfig",
    "GraphThresholdingConfig",
    "SubgraphSelectionConfig",
    "CleanGraphConfig",
    "ResourceManager",
    "COMPLEXITY_COST_MAPPING",
    "RescalingMethod",
]


class AlgorithmNominator:
    """Select applicable graph algorithms based on graph properties and resource
    constraints.
    """

    def __init__(
        self,
        applicability_dict: dict[str, dict[str, Any]],
        resource_manager: ResourceManager,
        include_algorithms: list[str] | None = None,
        exclude_algorithms: list[str] | None = None,
        enable_classification: bool = True,
        enable_resource_constraints: bool = True,
    ):
        """Initialize the AlgorithmNominator.

        Parameters
        ----------
        applicability_dict : Dict[str, Dict[str, Any]]
            Dictionary containing algorithm applicability conditions.
        resource_manager : ResourceManager
            Manager to handle resource constraints.
        """
        self.applicability_dict = applicability_dict
        self.resource_manager = resource_manager
        self.include_algorithms = (
            set(include_algorithms) if include_algorithms else set()
        )
        self.exclude_algorithms = (
            set(exclude_algorithms) if exclude_algorithms else set()
        )
        self.enable_classification = enable_classification
        self.enable_resource_constraints = enable_resource_constraints
        self._algorithms_lock = Lock()

    def select_algorithms(
        self,
        graph_properties: GraphProperties,
        query: str | None,
        intent: list[Intent] | None = None,
    ) -> list[str]:
        """Select algorithms applicable to the given graph properties.

        Parameters
        ----------
        graph_properties : GraphProperties
            Precomputed properties of the graph.
        query : str or None
            The user's query.
        intent : List[Intent] or None
            A list of `Intent` objects.

        Returns
        -------
        List[str]
            List of selected algorithm names.
        """
        if not self.enable_classification:
            elected = [
                alg
                for alg in self.include_algorithms
                if alg not in self.exclude_algorithms and alg in self.applicability_dict
            ]
            logger.info(
                f"Classification disabled. Selected algorithms based on inclusion and "
                f"exclusion: {elected}"
            )
            return elected

        with self._algorithms_lock:
            num_nodes = graph_properties.num_nodes
            num_edges = graph_properties.num_edges
            selected_algorithms = []

            logger.info(
                f"Selecting applicable algorithms for graph with {num_nodes} nodes "
                f"and {num_edges} edges."
            )

            for alg, conditions in self.applicability_dict.items():
                logger.debug(f"Evaluating applicability for algorithm: '{alg}'")
                if self._is_applicable(graph_properties, conditions):
                    if self.enable_resource_constraints:
                        time_complexity = conditions.get(
                            "time_complexity", "unknown"
                        ).lower()
                        space_complexity = conditions.get(
                            "space_complexity", "unknown"
                        ).lower()

                        time_cost_func = COMPLEXITY_COST_MAPPING.get(time_complexity)
                        space_cost_func = COMPLEXITY_COST_MAPPING.get(space_complexity)

                        if not time_cost_func or not space_cost_func:
                            logger.warning(
                                f"Algorithm '{alg}' has unknown complexity types "
                                f"(Time: '{time_complexity}', Space: "
                                f"'{space_complexity}'). Excluding from selection."
                            )
                            continue

                        estimated_time = time_cost_func(num_nodes, num_edges)
                        estimated_space = space_cost_func(num_nodes, num_edges)

                        logger.debug(
                            f"Estimated costs for '{alg}': Time = {estimated_time}, "
                            f"Space = "
                            f"{estimated_space}"
                        )

                        if self.resource_manager.is_within_limits(
                            estimated_time, estimated_space
                        ):
                            selected_algorithms.append(alg)
                            logger.info(
                                f"Algorithm '{alg}' is selected (Estimated Time: "
                                f"{estimated_time}, "
                                f"Estimated Space: {estimated_space})."
                            )
                        else:
                            logger.warning(
                                f"Algorithm '{alg}' excluded due to resource "
                                f"constraints (Estimated Time: {estimated_time}, "
                                f"Estimated Space: {estimated_space})."
                            )
                    else:
                        selected_algorithms.append(alg)
                else:
                    logger.debug(
                        f"Algorithm '{alg}' is not applicable based on graph "
                        f"properties."
                    )

            if self.exclude_algorithms:
                selected_algorithms = [
                    alg
                    for alg in selected_algorithms
                    if alg not in self.exclude_algorithms
                ]
                logger.info(f"Algorithms after exclusion: {selected_algorithms}")

            if self.include_algorithms:
                included = [
                    alg
                    for alg in self.include_algorithms
                    if alg in self.applicability_dict
                ]
                selected_algorithms.extend(
                    [alg for alg in included if alg not in selected_algorithms]
                )
                logger.info(f"Algorithms after inclusion: {selected_algorithms}")

            if query:
                selected_algorithms = filter_path_algorithms(
                    selected_algorithms, query, intent
                )

            logger.info(f"Selected algorithms: {selected_algorithms}")
            return selected_algorithms

    def _is_applicable(
        self, graph_props: GraphProperties, conditions: dict[str, Any]
    ) -> bool:
        """Determine if an algorithm is applicable to the given graph based on its
        conditions.

        Parameters
        ----------
        graph_props : GraphProperties
            Precomputed properties of the graph.
        conditions : Dict[str, Any]
            Applicability conditions for the algorithm.

        Returns
        -------
        bool
            True if applicable, False otherwise.
        """
        # Directedness
        if "directed" in conditions:
            if conditions["directed"] is True and not graph_props.is_directed:
                logger.debug(
                    "Algorithm requires a directed graph, but the graph is undirected."
                )
                return False
            if conditions["directed"] is False and graph_props.is_directed:
                logger.debug(
                    "Algorithm requires an undirected graph, but the graph is directed."
                )
                return False

        # Requires Unweighted
        if "requires_unweighted" in conditions:
            if conditions["requires_unweighted"] is True and graph_props.is_weighted:
                logger.debug(
                    "Algorithm requires an unweighted graph, but the graph is weighted."
                )
                return False

        # Requires Looplessness
        if "requires_looplessness" in conditions:
            has_self_loops = any(u == v for u, v in graph_props.graph.edges())
            if conditions["requires_looplessness"] is True and has_self_loops:
                logger.debug(
                    "Algorithm requires looplessness, but the graph has self-loops."
                )
                return False

        # Requires Symmetry (i.e., undirected or symmetric directed edges)
        if "requires_symmetry" in conditions:
            if conditions["requires_symmetry"]:
                if graph_props.is_directed:
                    # Check if for every edge (u, v), the edge (v, u) exists
                    symmetry = all(
                        graph_props.graph.has_edge(v, u)
                        for u, v in graph_props.graph.edges()
                    )
                    if not symmetry:
                        logger.debug(
                            "Algorithm requires symmetry, but the graph is not "
                            "symmetric."
                        )
                        return False
                else:
                    # Undirected graphs are symmetric by nature
                    pass

        # Requires Connectedness
        if "requires_connectedness" in conditions:
            if conditions["requires_connectedness"] and not graph_props.is_connected:
                logger.debug(
                    "Algorithm requires a connected graph, but it is disconnected."
                )
                return False

        # Requires Strongly Connected
        if "requires_strongly_connected" in conditions:
            if (
                conditions["requires_strongly_connected"]
                and not graph_props.is_strongly_connected
            ):
                logger.debug(
                    "Algorithm requires a strongly connected graph, but it is not."
                )
                return False

        # Requires Weakly Connected
        if "requires_weakly_connected" in conditions:
            if conditions["requires_weakly_connected"] and not graph_props.is_connected:
                logger.debug(
                    "Algorithm requires a weakly connected graph, but it is not."
                )
                return False

        # Requires DAG (Directed Acyclic Graph)
        if "requires_dag" in conditions:
            if conditions["requires_dag"] and not nx.is_directed_acyclic_graph(
                graph_props.graph
            ):
                logger.debug("Algorithm requires a DAG, but the graph is not a DAG.")
                return False

        # Requires Tree
        if "requires_tree" in conditions:
            if conditions["requires_tree"] and not graph_props.is_tree:
                logger.debug("Algorithm requires a tree, but the graph is not a tree.")
                return False

        # Requires Bipartite
        if "bipartite" in conditions:
            if conditions["bipartite"] and not graph_props.is_bipartite:
                logger.debug("Algorithm requires a bipartite graph, but it is not.")
                return False

        # Requires Multigraph
        if "multigraph" in conditions:
            if conditions["multigraph"] and not graph_props.is_multigraph:
                logger.debug("Algorithm requires a multigraph, but the graph is not.")
                return False
            if not conditions["multigraph"] and graph_props.is_multigraph:
                logger.debug(
                    "Algorithm requires a simple graph, but the graph is a multigraph."
                )
                return False

        # Requires Simple Graph
        if "simple_graph" in conditions:
            if conditions["simple_graph"] and graph_props.is_multigraph:
                logger.debug(
                    "Algorithm requires a simple graph, but the graph is a multigraph."
                )
                return False

        # Node and Edge Counts
        if "min_nodes" in conditions:
            if graph_props.num_nodes < conditions["min_nodes"]:
                logger.debug(
                    f"Algorithm requires at least {conditions['min_nodes']} nodes, "
                    f"but the graph has {graph_props.num_nodes} nodes."
                )
                return False
        if "max_nodes" in conditions:
            if graph_props.num_nodes > conditions["max_nodes"]:
                logger.debug(
                    f"Algorithm requires at most {conditions['max_nodes']} nodes, "
                    f"but the graph has {graph_props.num_nodes} nodes."
                )
                return False
        if "min_edges" in conditions:
            if graph_props.num_edges < conditions["min_edges"]:
                logger.debug(
                    f"Algorithm requires at least {conditions['min_edges']} edges, "
                    f"but the graph has {graph_props.num_edges} edges."
                )
                return False
        if "max_edges" in conditions:
            if graph_props.num_edges > conditions["max_edges"]:
                logger.debug(
                    f"Algorithm requires at most {conditions['max_edges']} edges, "
                    f"but the graph has {graph_props.num_edges} edges."
                )
                return False

        # Data Presence
        if "has_edge_data" in conditions:
            if conditions["has_edge_data"] and not graph_props.has_edge_data:
                logger.debug(
                    "Algorithm requires edge data, but the graph's edges lack data."
                )
                return False

        # Density
        if "density" in conditions:
            density_condition = conditions["density"]
            if isinstance(density_condition, str):
                if density_condition == "dense" and graph_props.density < 0.5:
                    logger.debug(
                        f"Algorithm requires a dense graph, but the density is "
                        f"{graph_props.density:.2f}."
                    )
                    return False
                if density_condition == "sparse" and graph_props.density >= 0.5:
                    logger.debug(
                        f"Algorithm requires a sparse graph, but the density is "
                        f"{graph_props.density:.2f}."
                    )
                    return False
            elif (
                isinstance(density_condition, (tuple, list))
                and len(density_condition) == 2
            ):
                min_density, max_density = density_condition
                if not (min_density <= graph_props.density <= max_density):
                    logger.debug(
                        f"Algorithm requires density between {min_density} and "
                        f"{max_density}, "
                        f"but the density is {graph_props.density:.2f}."
                    )
                    return False

        # Planarity
        if "planar" in conditions:
            if conditions["planar"] and not graph_props.is_planar:
                logger.debug(
                    "Algorithm requires a planar graph, but the graph is not planar."
                )
                return False

        # Cycles
        if "has_cycles" in conditions:
            has_cycles = graph_props.is_cyclical
            if conditions["has_cycles"] and not has_cycles:
                logger.debug(
                    "Algorithm requires a graph with cycles, but the graph has none."
                )
                return False
            if not conditions["has_cycles"] and has_cycles:
                logger.debug(
                    "Algorithm requires an acyclic graph, but the graph has cycles."
                )
                return False

        logger.debug("Algorithm is applicable based on graph properties.")
        return True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Clean up resources and handle any exceptions during context exit.

        Parameters
        ----------
        exc_type : type
            The exception type, if an exception occurred.
        exc_value : Exception
            The exception instance, if an exception occurred.
        traceback : TracebackType
            The traceback object, if an exception occurred.

        Returns
        -------
        bool
            True if the exception was handled, False otherwise.
        """
        try:
            self.resource_manager.release()
            logger.info("Resources released successfully in AlgorithmNominator.")
        except Exception:
            logger.exception("Error during resource cleanup in __exit__")

        if exc_type is not None:
            logger.error(
                f"Exception occurred in AlgorithmNominator: {exc_type} - {exc_value}"
            )
            return False

        logger.info("AlgorithmNominator exited cleanly.")
        return True


class AlgorithmElector:
    """Elect and apply graph algorithms based on user queries and graph summaries."""

    def __init__(
        self,
        algorithm_docs: dict[str, str],
        applicability_dict: dict[str, dict[str, Any]],
        include_algorithms: list[str] | None = None,
        exclude_algorithms: list[str] | None = None,
        enable_classification: bool = True,
    ):
        """Initialize the AlgorithmElector.

        Parameters
        ----------
        algorithm_docs : Dict[str, str]
            Dictionary containing documentation strings for algorithms.
        applicability_dict : Dict[str, Dict[str, Any]]
            Dictionary containing algorithm applicability conditions.
        """
        self.zero_shot_classifier = pipeline(
            "zero-shot-classification", model="facebook/bart-large-mnli", device=-1
        )
        self.algorithm_docs = algorithm_docs
        self.applicability_dict = applicability_dict
        self.include_algorithms = (
            set(include_algorithms) if include_algorithms else set()
        )
        self.exclude_algorithms = (
            set(exclude_algorithms) if exclude_algorithms else set()
        )
        self.enable_classification = enable_classification
        self._cleanup_lock = Lock()
        self._is_cleaned_up = False

    def elect_algorithms(
        self,
        query: str | None,
        graph_summary: str,
        user_intent: list[Intent],
        candidates: list[str],
        top_n: int = 5,
    ) -> list[str]:
        """Select algorithms using zero-shot classification based on query and graph
        summary.

        Parameters
        ----------
        query : str or None
            The user's query.
        graph_summary : str
            Summary of the graph structure and properties.
        user_intent : List[Intent]
            List of high-level intents detected.
        candidates : List[str]
            List of applicable algorithms to choose from.
        top_n : int, optional
            Number of top algorithms to select, by default 5.

        Returns
        -------
        List[str]
            List of selected algorithm names.
        """
        if not self.enable_classification:
            elected = [alg for alg in self.include_algorithms if alg in candidates]
            logger.info(
                f"Classification disabled. Elected algorithms based on inclusion: "
                f"{elected}"
            )
            return elected

        intent_descriptions = [intent.value for intent in user_intent]

        candidate_descriptions = [
            self.algorithm_docs.get(alg, "") for alg in candidates
        ]

        if not any(candidate_descriptions):
            raise ValueError("No candidate algorithm descriptions found.")

        prompt_template = """
            Given the user query: '{query}', the graph summary: '{graph_summary}',
            and the user's intents: '{intents}', which of the networkx algorithms would
            yield the most relevant insights to assist in responding helpfully to the
            user query?
        """

        # Handle None query by substituting with an empty string
        escaped_query = re.escape(query) if query else ""
        escaped_graph_summary = re.escape(graph_summary)
        escaped_intents = ", ".join(map(re.escape, intent_descriptions))

        prompt = prompt_template.format(
            query=escaped_query,
            graph_summary=escaped_graph_summary,
            intents=escaped_intents,
        )

        try:
            result = self.zero_shot_classifier(
                prompt, candidate_descriptions, multi_label=True
            )
        except Exception as e:
            logger.exception("Error during zero-shot classification")
            raise RuntimeError("Error during zero-shot classification") from e

        if not isinstance(result, dict) or "scores" not in result:
            logger.error("Unexpected result format from zero-shot classifier.")
            raise RuntimeError("Unexpected result format from zero-shot classifier.")

        # Ensure that scores align with candidates
        if len(result["scores"]) != len(candidates):
            logger.error(
                "Mismatch between number of candidates and number of scores returned."
            )
            raise RuntimeError(
                "Mismatch between number of candidates and number of scores returned."
            )

        algorithm_scores = list(zip(candidates, result["scores"]))
        sorted_algorithms = sorted(algorithm_scores, key=lambda x: x[1], reverse=True)
        top_algorithms = sorted_algorithms[:top_n]

        elected_algorithms = [alg for alg, _ in top_algorithms]

        logger.info(f"Classified top algorithms: {elected_algorithms}")

        if self.exclude_algorithms:
            elected_algorithms = [
                alg for alg in elected_algorithms if alg not in self.exclude_algorithms
            ]
            logger.info(f"Algorithms after exclusion: {elected_algorithms}")

        if self.include_algorithms:
            for alg in self.include_algorithms:
                if alg not in elected_algorithms and alg in candidates:
                    elected_algorithms.append(alg)
                    logger.info(f"Algorithm '{alg}' included as per user preference.")

        logger.info(f"Final elected algorithms: {elected_algorithms}")
        return elected_algorithms

    def apply_elected_algorithms(
        self,
        graph: nx.Graph,
        algorithms: list[str],
        query: str | None,
        user_intent: list[Intent],
    ) -> dict[str, Any]:
        """Apply elected algorithms to the graph and map their results.

        Parameters
        ----------
        graph : nx.Graph
            The graph to analyze.
        algorithms : List[str]
            List of algorithms to apply.
        query : str or None
            The user's query.

        Returns
        -------
        Dict[str, Any]
            Dictionary of algorithm results.
        """
        results = {}

        # analyze the query once since it doesn't change per algorithm
        if query:
            analyzer = PathQueryAnalyzer()
            has_source, has_target, path_intents = analyzer.analyze_query(
                query, user_intent
            )
        else:
            has_source, has_target, path_intents = False, False, set()

        def apply_algorithm_safe(algorithm, kwargs):
            """Apply a single algorithm and handle exceptions."""
            result = None
            try:
                result = apply_algorithm(
                    self.applicability_dict, graph, algorithm, **kwargs
                )
                map_algorithm_result(graph, algorithm, result)
                logger.info(f"Applied algorithm '{algorithm}' successfully.")
                return result  # ruff: skip # noqa: TRY300
            except KeyboardInterrupt:
                logger.info("Process interrupted by user during algorithm application.")
                raise
            except Exception as e:
                error_message = f"Error applying algorithm '{algorithm}': {e}"
                logger.exception(error_message)
                return error_message

        for algorithm in algorithms:
            # compute kwargs for each algorithm
            kwargs = self.extract_algorithm_parameters(
                query, algorithm, has_source, has_target, path_intents
            )
            results[algorithm] = apply_algorithm_safe(algorithm, kwargs)
        return results

    @staticmethod
    def extract_algorithm_parameters(
        query: str | None,
        algorithm_name: str,
        has_source: bool,
        has_target: bool,
        path_intents: set[PathIntent],
    ) -> dict[str, Any]:
        """Extract algorithm parameters using comprehensive path semantics.

        Parameters
        ----------
        query : Optional[str]
            The user's query.
        algorithm_name : str
            The name of the algorithm.
        has_source : bool
            Whether query indicates source node.
        has_target : bool
            Whether query indicates target node.
        path_intents : Set[PathIntent]
            Detected path intents in query.

        Returns
        -------
        Dict[str, Any]
            Dictionary of algorithm parameters.
        """
        parameters = {}
        if not query:
            return parameters

        query = query.lower()
        concepts = PathConcepts()

        extractor = EntityExtractor()

        # algorithms requiring both source and target
        if algorithm_name in {
            "shortest_path",
            "dijkstra_path",
            "bellman_ford_path",
            "shortest_simple_paths",
        }:
            source = None
            target = None

            if has_source:
                sources = extractor.extract_entities(
                    query,
                    concepts.SOURCE_INDICATORS,
                )
                source = sources[0] if sources else None

            if has_target:
                targets = extractor.extract_entities(
                    query,
                    concepts.TARGET_INDICATORS,
                )
                target = targets[-1] if targets else None

            # For causal/diagnostic intents, try additional indicators
            if not source and PathIntent.CAUSAL_PATH in path_intents:
                sources = extractor.extract_entities(query, concepts.CAUSAL_INDICATORS)
                source = sources[0] if sources else None
            if not target and PathIntent.DIAGNOSTIC_PATH in path_intents:
                targets = extractor.extract_entities(
                    query, concepts.CAUSAL_INDICATORS | concepts.FLOW_INDICATORS
                )
                target = targets[-1] if targets else None

            if source and target:
                logger.info(f"Source: {source} --> target: {target}")
                parameters["source"] = source
                parameters["target"] = target
            else:
                logger.warning(
                    f"Could not determine both source and target nodes for "
                    f"'{algorithm_name}'. Source: {source}, Target: {target}"
                )
                parameters["source"] = source
                parameters["target"] = target

        # algorithms requiring only source
        elif algorithm_name in {
            "single_source_shortest_path",
            "single_source_dijkstra_path",
            "single_source_bellman_ford_path",
        }:
            source = None
            if has_source:
                sources = extractor.extract_entities(
                    query,
                    concepts.SOURCE_INDICATORS,
                )
                source = sources[0] if sources else None

            # for influence/diagnostic intents, try additional indicators
            if not source and (
                PathIntent.INFLUENCE_PATH in path_intents
                or PathIntent.DIAGNOSTIC_PATH in path_intents
            ):
                sources = extractor.extract_entities(
                    query, concepts.CAUSAL_INDICATORS | concepts.FLOW_INDICATORS
                )
                source = sources[0] if sources else None

            if source:
                parameters["source"] = source
            else:
                logger.warning(
                    f"Could not determine source node for '{algorithm_name}'."
                )
                parameters["source"] = None

        return parameters

    @property
    def algorithm_classifier(self):
        logger.info("Accessing algorithm_classifier.")
        return self._algorithm_classifier

    @algorithm_classifier.setter
    def algorithm_classifier(self, value):
        logger.info("Setting algorithm_classifier.")
        self._algorithm_classifier = value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        """Explicitly clean up resources."""
        with self._cleanup_lock:
            if not self._is_cleaned_up:
                logger.info("Cleaning up AlgorithmElector resources.")
                try:
                    if (
                        hasattr(self, "zero_shot_classifier")
                        and self.zero_shot_classifier
                    ):
                        del self.zero_shot_classifier
                        self.zero_shot_classifier = None
                        logger.info("Zero-shot classifier pipeline deleted.")
                except Exception:
                    logger.exception("Error during cleanup in close")
                finally:
                    self._is_cleaned_up = True
                    logger.info("AlgorithmElector cleanup complete.")


class GraphPreprocessingSelector:
    """Predicts which preprocessing steps to apply based on the graph and the
    algorithms.
    """

    def __init__(self, algorithm_applicability: dict[str, dict[str, Any]]):
        """Initialize the GraphPreprocessingSelector.

        Parameters
        ----------
        algorithm_applicability : Dict[str, Dict[str, Any]]
            Dictionary containing algorithm applicability conditions.
        """
        self.algorithm_applicability = algorithm_applicability

    def select_preprocessing_steps(
        self, graph: nx.Graph, algorithms: list[str]
    ) -> CleanGraphConfig:
        """Determine the necessary preprocessing steps based on the graph and selected
        algorithms.

        Parameters
        ----------
        graph : nx.Graph
            The input graph.
        algorithms : List[str]
            List of algorithms to be applied.

        Returns
        -------
        CleanGraphConfig
            Configuration object specifying preprocessing steps.
        """
        logger.info("Predicting preprocessing steps based on selected algorithms.")

        config = CleanGraphConfig(
            force_symmetry=False,
            remove_self_loops=False,
            threshold=None,
            subgraph=None,
            rescale=None,
        )

        requires_symmetry = False
        requires_self_loops_removal = False
        requires_rescaling = False
        requires_connectedness = False
        rescaling_methods = set()

        for alg in algorithms:
            conditions = self.algorithm_applicability.get(alg, {})
            if not conditions:
                logger.warning(
                    f"No applicable conditions found for algorithm '{alg}'. Skipping."
                )
                continue

            if conditions.get("requires_symmetry", False):
                requires_symmetry = True

            if not conditions.get("self_loops", True):
                requires_self_loops_removal = True

            if conditions.get("weighted", False):
                requires_rescaling = True
                rescaling_methods.add(RescalingMethod.normalize)

            if conditions.get("requires_connectedness", False):
                requires_connectedness = True

        # apply aggregated preprocessing configurations
        # 1. Force Symmetry
        if requires_symmetry:
            config.force_symmetry = True
            logger.info("Configured to force symmetry in the graph.")

        # 2. Remove Self-Loops
        if requires_self_loops_removal or nx.number_of_selfloops(graph) > 0:
            config.remove_self_loops = True
            logger.info("Configured to remove self-loops from the graph.")

        # 3. Rescale Graph
        if requires_rescaling:
            if rescaling_methods:
                selected_rescaling = rescaling_methods.pop()
                config.rescale = GraphRescalingConfig(method=selected_rescaling)
                logger.info(
                    f"Configured to rescale the graph using method: "
                    f"{selected_rescaling.value}."
                )

        # 4. Apply Merged Subgraph Selection Configuration
        if requires_connectedness:
            config.subgraph = self._select_subgraph_method(
                graph, SubgraphSelectionConfig()
            )
            logger.info(f"Subgraph selection: {config.subgraph}")

        logger.info(f"Final preprocessing configuration: {config}")
        return config

    @staticmethod
    def _select_subgraph_method(
        G: nx.Graph, config: SubgraphSelectionConfig
    ) -> SubgraphSelectionConfig:
        """Determine which subgraph selection method to apply."""
        connected_components = list(get_connected_components(G))
        num_components = len(connected_components)

        # more than 1 connected comp
        if num_components > 1:
            if config.min_nodes:
                # small components that need pruning
                small_components = [
                    comp
                    for comp in connected_components
                    if len(comp) < config.min_nodes
                ]
                if len(small_components) > 0:
                    config.prune_components = True
                    logger.debug("Merged 'prune_components' flag set to True.")
                    return config

            logger.debug("Merged 'use_lcc' flag set to True.")
            config.use_lcc = True
            return config

        # isolates
        isolates = [n for n, d in G.degree() if d == 0]
        if len(isolates) > 0 and config.defragment:
            config.defragment = True
            logger.debug("Merged 'defragment' flag set to True.")
            return config

        return config
