import importlib.resources as importlib_resources
import logging
import re
import warnings
from pathlib import Path

import nltk
from nltk.corpus import stopwords
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

from nxlu.explanation.corpus import load_corpus

nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)

warnings.filterwarnings("ignore")

logger = logging.getLogger("nxlu")

STOP_WORDS = set(stopwords.words("english"))

__all__ = ["EntityExtractor"]


class EntityExtractor:
    """A class to manage loading and using the BERT model for entity extraction."""

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
        self.model = AutoModelForTokenClassification.from_pretrained(
            "dslim/bert-base-NER", ignore_mismatched_sizes=True
        )
        self.ner_pipeline = pipeline(
            "ner",
            model=self.model,
            tokenizer=self.tokenizer,
            aggregation_strategy="simple",
            device=-1,
        )
        try:
            with importlib_resources.open_text(
                "nxlu.data", "graph_theory_corpus.txt"
            ) as f:
                self.graph_theory_keywords = set(load_corpus(Path(f.name)))
        except FileNotFoundError:
            logger.exception("Graph theory corpus file not found.")
            self.graph_theory_keywords = set()
        except Exception:
            logger.exception("Error loading the graph theory corpus.")
            self.graph_theory_keywords = set()

    def extract_entities(self, query: str, indicators: set[str]) -> list[str]:
        """Extract entities based on the indicators using the bert-base NER model.

        Parameters
        ----------
        query : str
            The user's input query string to analyze.
        indicators : Set[str]
            Set of indicator keywords relevant to the extraction process.

        Returns
        -------
        List[str]
            List of identified entities matching the provided indicators.
        """
        ner_results = self.ner_pipeline(query)

        # build a list of entities
        entities = [
            {
                "text": entity["word"],
                "type": entity["entity_group"],
                "start": entity["start"],
                "end": entity["end"],
            }
            for entity in ner_results
        ]

        # get positions of indicators in query
        indicators_positions = [
            {"indicator": indicator, "start": match.start(), "end": match.end()}
            for indicator in indicators
            for match in re.finditer(
                r"\b" + re.escape(indicator) + r"\b", query.lower()
            )
        ]

        # for each indicator position, find the entity that immediately proceeds it
        extracted_entities = []
        for ind_pos in indicators_positions:
            ind_end = ind_pos["end"]
            for entity in entities:
                if entity["start"] >= ind_end:
                    extracted_entities.append(entity["text"])
                    break

        return list(set(extracted_entities))

    def extract_all_entities(self, query: str) -> list[str]:
        """Extract all entities from the query using the NER model.

        Parameters
        ----------
        query : str
            The user's input query string to analyze.

        Returns
        -------
        List[str]
            List of identified entities.
        """
        # use NER pipeline
        ner_results = self.ner_pipeline(query)
        ner_entities = {entity["word"] for entity in ner_results}

        # use POS tagging for nouns, plural nouns, and numbers
        tokens = nltk.word_tokenize(query)
        pos_tags = nltk.pos_tag(tokens)
        pos_entities = {
            word
            for word, pos in pos_tags
            if pos.startswith(("NN", "NNS")) or pos == "CD"
        }

        pos_entities_filtered = {
            word for word in pos_entities if word.lower() not in STOP_WORDS
        }

        corpus_entities = {
            word for word in tokens if word.lower() in self.graph_theory_keywords
        }

        extracted_entities = ner_entities.union(pos_entities_filtered, corpus_entities)
        return list(extracted_entities)
