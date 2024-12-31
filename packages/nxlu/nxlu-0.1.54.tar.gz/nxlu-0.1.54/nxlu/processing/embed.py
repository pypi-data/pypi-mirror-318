import logging
import warnings
from pathlib import Path
from typing import Any

import numpy as np
import torch
from huggingface_hub import PyTorchModelHubMixin
from sentence_transformers import SentenceTransformer
from torch import nn
from transformers import AutoModel
from transformers import logging as tlogging

from nxlu.config import Precision

warnings.filterwarnings("ignore")

tlogging.set_verbosity_error()

logger = logging.getLogger("nxlu")

__all__ = ["CustomModel", "SentenceTransformerEmbedding"]


class CustomModel(nn.Module, PyTorchModelHubMixin):
    """Custom neural network model for domain classification.

    Attributes
    ----------
    model : transformers.AutoModel
        The pre-trained transformer model.
    dropout : torch.nn.Dropout
        Dropout layer for regularization.
    fc : torch.nn.Linear
        Fully connected layer for classification.
    """

    def __init__(self, config):
        super().__init__()
        self.model = AutoModel.from_pretrained(
            config["base_model"], ignore_mismatched_sizes=True
        )
        self.dropout = nn.Dropout(config["fc_dropout"])
        self.fc = nn.Linear(self.model.config.hidden_size, len(config["id2label"]))

    def forward(self, input_ids, attention_mask):
        """Forward pass through the network.

        Parameters
        ----------
        input_ids : torch.Tensor
            Token IDs.
        attention_mask : torch.Tensor
            Attention masks.

        Returns
        -------
        torch.Tensor
            Softmax probabilities for each class.
        """
        features = self.model(
            input_ids=input_ids, attention_mask=attention_mask
        ).last_hidden_state
        dropped = self.dropout(features)
        outputs = self.fc(dropped)
        return torch.softmax(outputs[:, 0, :], dim=1)


class SentenceTransformerEmbedding:
    """A class to handle text embeddings using SentenceTransformer."""

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
        batch_size: int = 32,
        cache_dir: str = str(Path.home() / "nxlu_cache"),
        precision: Precision = Precision.FLOAT32,
    ):
        """Initialize the SentenceTransformer model.

        Parameters
        ----------
        model_name : str
            The name of the pre-trained embedding model.
        batch_size : int
            The size of chunks to use to embed the data. Default is 32.
        """
        self.batch_size = batch_size
        self.model_name = model_name
        self.precision = precision
        self.cache_dir = cache_dir
        try:
            self.model = SentenceTransformer(
                self.model_name,
                cache_folder=self.cache_dir,
                model_kwargs={
                    "torch_dtype": self.precision,
                },
            )
        except Exception:
            logger.exception(f"Failed to load SentenceTransformer model '{model_name}'")
            raise

    def get_query_embedding(self, query: str) -> np.ndarray:
        """Get embedding for a single query string.

        Parameters
        ----------
        query : str
            The query string.

        Returns
        -------
        np.ndarray
            The array of embedding vectors.
        """
        try:
            embedding = self.model.encode(
                [query],
                convert_to_numpy=True,
            )
        except Exception:
            logger.exception("Failed to encode query")
            raise
        else:
            return embedding

    def get_text_embeddings(self, texts: list[Any]) -> np.ndarray:
        """Get embeddings for a list of text strings.

        Parameters
        ----------
        texts : list[Any]
            The list of text strings or any objects that can be converted to strings.

        Returns
        -------
        np.ndarray
            The array of embedding vectors.
        """
        try:
            texts = [str(text) for text in texts]
            embeddings = self.model.encode(
                texts,
                batch_size=self.batch_size,
                show_progress_bar=True,
                convert_to_numpy=True,
            )
        except Exception:
            logger.exception("Failed to encode texts")
            raise
        else:
            return embeddings
