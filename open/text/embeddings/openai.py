"""Wrapper around OpenAI embedding models that work with llama-cpp-python[server] package."""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field

from langchain.embeddings.base import Embeddings

DEFAULT_MODEL_NAME = ""


class OpenAIEmbeddings(BaseModel, Embeddings):
    """Wrapper around OpenAI embedding models that work with llama-cpp-python[server] package.

    To use, you should have the ``openai`` python package installed.

    Example:
        .. code-block:: python

            from custom.embeddings.openai import OpenAIEmbeddings
            embeddings = OpenAIEmbeddings()
    """

    client: Any  #: :meta private:
    model_name: str = DEFAULT_MODEL_NAME
    """Model name to use."""
    openai_api_base: str

    def __init__(self, **kwargs: Any):
        """Initialize the OpenAIEmbeddings"""
        super().__init__(**kwargs)
        try:
            import openai

        except ImportError as exc:
            raise ImportError(
                "Could not import openai python package. "
                "Please install it with `pip install openai`."
            ) from exc

        self.client = openai.Embedding

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Compute doc embeddings using underlying model of llama-cpp-python.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        texts = list(map(lambda x: x.replace("\n", " "), texts))
        embeddings = self.client.create(
            model=self.model_name,
            input=texts,
            api_base=self.openai_api_base
        )
        return [item["embedding"] for item in embeddings['data']]

    def embed_query(self, text: str) -> List[float]:
        """Compute query embeddings using underlying model of llama-cpp-python.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        text = text.replace("\n", " ")
        embeddings = self.client.create(
            model=self.model_name,
            input=text,
            api_base=self.openai_api_base
        )
        return embeddings['data'][0]['embedding']
