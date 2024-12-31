[![Python](https://img.shields.io/pypi/pyversions/nxlu.svg)](https://badge.fury.io/py/nxlu)
[![PyPI](https://badge.fury.io/py/nxlu.svg)](https://badge.fury.io/py/nxlu)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Network Language Understanding (NxLU)

<p align="center">
  <img src="doc/_static/NXLU_logo.png" alt="NxLU Logo" width="150"/>
</p>

## Table of Contents

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage (Dispatch)](#usage-dispatch)
- [Enabling NxLU Backend](#enabling-nxlu-backend)
- [Multi-Hop Graph Reasoning](#multi-hop-graph-reasoning)
- [Architecture](#architecture)
- [Usage (Reasoning)](#usage-reasoning)
- [Citation](#citation)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The practice of analyzing networks is unique in that the symbolic operations (i.e. graph algorithms) used to characterize their topology are well-defined and objective, yet their applicability and the interpretion of their outputs, can be highly nuanced and subjective.

`NxLU` is a framework that attempts to reduce researcher bias in network analysis and reduce the cognitive load on practitioners by automating graph topological inference through LLM-generated interpretation of graph metrics *in media res*. By combining quantitative descriptions of networks with RAG-constrained qualitative insights, `NxLU` aims to bridge the gap between precise structural analysis and human-like interpretability so as to democratize network analysis across a broad audience while promoting a more rigorous network science.

## System Requirements

NxLU runs on Python version 3.10 or higher and NetworkX version 3.0 or higher, and requires the following additional non-standard dependencies:

- PyTorch version 2.2 or higher
- Transformers version 4.43 or higher
- Sentence-Transformers version 3.0 or higher
- LangChain version 0.3 or higher
- Llama-Index version 0.11 or higher
- Huggingface-Hub version 0.24 or higher

For a complete list of dependencies, please refer to the pyproject.toml file in the project repository.

## Installation

For the default installation of NxLU (using LangChain), run the following command:
```bash
pip install nxlu
```

To leverage the Llamaindex framework, run:
```bash
pip install nxlu[llamaindex]
```

Then, set up your API key:
```bash
export ANTHROPIC_API_KEY=YOUR_API_KEY
# or:
export OPENAI_API_KEY=YOUR_API_KEY
```

## Usage (Dispatch)

### Enabling NxLU Backend

To use NxLU as a backend for NetworkX, you can use any of the following methods that serve to activate NetworkX's [dispatch-plugin mechanism](https://networkx.org/documentation/stable/reference/backends.html):

1. **Environment Variable**:
   Set the `NETWORKX_AUTOMATIC_BACKENDS` environment variable to automatically dispatch to NxLU for supported APIs:

   ```bash
   export NETWORKX_AUTOMATIC_BACKENDS=nxlu
   python my_networkx_script.py
   ```

2. **Backend Keyword Argument**:
   Explicitly specify NxLU as the backend for particular API calls:

   ```python
   import os
   import networkx as nx

   nx.config.backends.nxlu.active = True

   nx.config.backends.nxlu.set_openai_api_key(os.getenv("OPENAI_API_KEY"))
   nx.config.backends.nxlu.set_model_name("gpt-4o-mini")
   ## or
   # nx.config.backends.nxlu.set_anthropic_api_key(os.getenv("ANTHROPIC_API_KEY"))
   # nx.config.backends.nxlu.set_model_name("claude-3.5-sonnet")

   G = nx.path_graph(4)
   nx.betweenness_centrality(G, backend="nxlu")
   ```

3. **Type-Based Dispatching**:

   ```python
   import networkx as nx
   from nxlu.core.interface import LLMGraph

   G = nx.path_graph(4)
   H = LLMGraph(G)

   nx.betweenness_centrality(H)
   ```

By integrating with NetworkX's backend system, NxLU provides a seamless way to enhance existing graph analysis workflows with advanced natural language processing and reasoning capabilities.

### Multi-Hop Graph Reasoning

#### Architecture

NxLU's multi-hop graph reasoning mode invokes a multi-hop strategy of "interrogating" a graph's topology (with or without a user query):

- **Dynamic Contextualization**: Leverages GraphRAG and semantic similarity to select query-relevant small-world subgraphs, adapting analysis to the specific needs of each query, ensuring relevant, computationally tractable, and precise network insights.
- **User Intent Detection**: Identifies the goal of the user's query using zero-shot classification.
- **Graph Characterization**: Describes the input graph's domain and structure.
- **Dynamic Algorithm Selection**: Leverages available graph attributes and user queries (if provided), along with rule-based mappings and zero-shot classification to select and rank suitable graph algorithms.
- **Dynamic Graph Preprocessing**: Infers an optimal preprocessing pipeline suitable for the graph and the dynamically selected algorithms.
- **Domain Agnostic Reasoning**: Designed to support various graph analysis tasks such as recommendations, explanations, diagnostics, clustering, and ranking. While versatile, NxLU is optimized for scenarios where integrating graph topology with natural language queries provides significant value.

### Usage (Reasoning)

In python, first set up the configuration:

```python
import os
import networkx as nx
from nxlu.explanation.explain import GraphExplainer
from nxlu.config import get_config, OpenAIModel, AnthropicModel

config = get_config()

## set an LLM framework (both LangChain and LlamaIndex are supported, though LangChain is the default)
# config.set_llm_framework("llamaindex")

openai_api_key = os.getenv("OPENAI_API_KEY")
config.set_openai_api_key(openai_api_key)
config.set_model_name("gpt-4o-mini") # default
## or
# anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
# config.set_anthropic_api_key(anthropic_api_key)
# config.set_model_name("claude-3.5-sonnet")
## or
# config.set_model_name("llama3:8b")

## Optional configuration parameters
config.set_verbosity_level(1)
config.set_max_tokens(500)
config.set_embedding_model_name("vinai/bertweet-base")
# config.set_temperature(0.1) # default
# config.set_num_thread(8) # default
# config.set_num_gpu(0) # default
## specify networkx algorithms by name to be included or excluded
# config.set_include_algorithms(['betweenness_centrality', 'clustering'])
# config.set_exclude_algorithms(['shortest_path'])
# config.set_enable_subgraph_retrieval(False) # the default is `True`, which enables an experimental FAISS-based subgraph selection mechanism will be used to retrieve a connected subgraph that captures the most semantically similar nodes and edges to the user's query. If restricted to cpu-only, limited RAM, or working with large dense graphs (e.g. >10,000 nodes), try setting this to `False`.
# config.set_enable_classification(False) # the default is `True`, but if this is set to `False`, the system should rely solely on the include/exclude lists without performing zero-shot classification of the most "suitable" algorithms for the graph + query.
# config.set_enable_resource_constraints(False) # the default is `True`, but if this is set to `False`, the system should ignore the resource constraints detected on the current hardware when determining which algorithms are suitable to run within tractable timeframes given the scale of the graph.
```

In the following minimal example, we use the GraphExplainer to analyze a social network graph, with or without a specific query. This example shows both cases:

```python
G = nx.Graph()

G.add_edge('Elon Musk', 'Jeff Bezos', weight=30)
G.add_edge('Elon Musk', 'Tim Cook', weight=15)
G.add_edge('Elon Musk', 'Sundar Pichai', weight=12)
G.add_edge('Elon Musk', 'Satya Nadella', weight=20)
G.add_edge('Jeff Bezos', 'Warren Buffet', weight=25)
G.add_edge('Jeff Bezos', 'Bill Gates', weight=10)
G.add_edge('Jeff Bezos', 'Tim Cook', weight=18)
G.add_edge('Tim Cook', 'Sundar Pichai', weight=8)
G.add_edge('Tim Cook', 'Sheryl Sandberg', weight=9)
G.add_edge('Sundar Pichai', 'Bill Gates', weight=6)
G.add_edge('Sundar Pichai', 'Sheryl Sandberg', weight=7)
G.add_edge('Satya Nadella', 'Warren Buffet', weight=15)
G.add_edge('Satya Nadella', 'Sheryl Sandberg', weight=13)
G.add_edge('Bill Gates', 'Warren Buffet', weight=40)

# Initialize the explainer with configuration
explainer = GraphExplainer(config)

# Perform analysis without a specific query
response = explainer.explain(G)
print(response)

# Perform analysis with a specific query
query = "Which executive in this network is the most connected to the other executives?"
response = explainer.explain(G, query)
print(response)
```

### Supported Models

NxLU supports a wide range of language models from different providers, including [ollama](https://ollama.com/library) local models. You can configure NxLU to use one of the following models based on your needs:

**OpenAI Models**:

- GPT-4 (gpt-4)
- GPT-4O (gpt-4o) (gpt-4o)
- GPT-4O Mini (gpt-4o-mini)
- GPT-4O1 Preview (o1-preview)
- GPT-401 Mini (o1-mini)

**Anthropic Models**:

- Claude 2 (claude-2)
- Claude 2.0 (claude-2.0)
- Claude Instant (claude-instant)
- Claude Instant 1 (claude-instant-1)
- Claude Instant 1.1 (claude-instant-1.1)
- Claude 3 Sonnet (claude-3-sonnet)
- Claude 3.5 Sonnet (claude-3.5-sonnet)

**Local Models**:

- Llama 3 - 70B (llama3:70b)
- Llama 3 - 8B (llama3:8b)
- Gemma 2 - 9B (gemma2:9b)
- Qwen 2 - 7B (qwen2:7b)

## Citation

A paper is forthcoming, but if you use `NxLU` in your research, please cite it as follows:

```latex
@article{alexander2024nxlu,
  author    = {Derek Alexander},
  title     = {NxLU: Network Language Understanding},
  note      = {in preparation},
  year      = {2024}
}
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to discuss potential improvements or features. Before submitting, ensure that you read and follow the [CONTRIBUTING](CONTRIBUTING) guide.

## License

This project is licensed under the [MIT License](LICENSE).
