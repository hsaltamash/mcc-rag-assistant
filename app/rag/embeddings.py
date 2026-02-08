"""Embedding stubs for vectorization."""

from typing import List


def embed_texts(texts: List[str]) -> List[List[float]]:
    """Return placeholder embeddings for each text chunk."""
    return [[float(len(text))] for text in texts]
