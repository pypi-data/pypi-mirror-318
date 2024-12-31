import os

from transformers import pipeline

from nxlu.config import Intent
from nxlu.utils.misc import most_common_element

if not os.environ.get("TOKENIZERS_PARALLELISM"):
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

__all__ = [
    "IntentClassifier",
    "classify_domain",
]


class IntentClassifier:
    """Classify high-level intents from a user's query using zero-shot
    classification.

    Attributes
    ----------
    classifier : transformers.pipeline
        The zero-shot classification pipeline using the BART model.

    Methods
    -------
    fit_transform(query: str, threshold: float) -> list[Intent]
        Classifies the query and returns the list of predicted intents.
    """

    def __init__(self):
        """
        Initialize the IntentClassifier class.

        The classifier uses a zero-shot classification pipeline with the
        'facebook/bart-large-mnli' model.
        """
        self.classifier = pipeline(
            "zero-shot-classification", model="facebook/bart-large-mnli", device=-1
        )

    def fit_transform(self, query: str, threshold: float = 0.6) -> list[Intent]:
        """
        Classify the given query into high-level intents using zero-shot
        classification.

        Parameters
        ----------
        query : str
            The user query to classify.
        threshold : float, optional
            The confidence threshold for selecting intents (default is 0.6).

        Returns
        -------
        list[Intent]
            A list of `Intent` objects that have confidence scores higher
            than the threshold.
        """
        candidate_labels = [intent.value for intent in Intent]
        results = self.classifier(query, candidate_labels, multi_label=True)

        # select intents with softmax confidence above a threshold
        selected_intents = [
            Intent(label.strip())
            for label, score in zip(results["labels"], results["scores"])
            if score > threshold
        ]

        return selected_intents


def classify_domain(attributes: dict) -> str:
    """Classify the domain based on node and edge attributes.

    Parameters
    ----------
    attributes : dict
        A dictionary containing attributes for nodes and edges. The
        'query' field is optional.

    Returns
    -------
    str
        The most common predicted domain based on the node and edge
        attributes and optional query.
    """
    import torch
    from transformers import AutoConfig, AutoTokenizer

    from nxlu.processing.embed import CustomModel

    config = AutoConfig.from_pretrained("nvidia/domain-classifier")
    tokenizer = AutoTokenizer.from_pretrained("nvidia/domain-classifier")
    model = CustomModel.from_pretrained("nvidia/domain-classifier")

    node_attributes = [str(node[1]) for node in attributes["nodes"]]
    edge_attributes = [str(edge) for edge in attributes["edges"]]

    input_strings = node_attributes + edge_attributes

    if attributes.get("query"):
        input_strings.append(attributes["query"])

    inputs = tokenizer(
        input_strings,
        return_tensors="pt",
        padding="longest",
        truncation=True,
    )
    outputs = model(inputs["input_ids"], inputs["attention_mask"])

    predicted_classes = torch.argmax(outputs, dim=1).cpu().numpy()
    predicted_domains = [config.id2label[class_idx] for class_idx in predicted_classes]

    return most_common_element(predicted_domains)
