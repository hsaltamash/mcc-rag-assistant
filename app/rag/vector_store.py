"""Vector store interface stubs."""

from dataclasses import dataclass
from typing import List


@dataclass
class VectorRecord:
    """In-memory vector record."""

    content: str
    embedding: List[float]


def build_records(texts: List[str], embeddings: List[List[float]]) -> List[VectorRecord]:
    """Create vector records from texts and embeddings."""
    return [VectorRecord(content=text, embedding=vector) for text, vector in zip(texts, embeddings)]
