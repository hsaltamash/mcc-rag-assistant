"""Retrieval interfaces for the assistant."""

from dataclasses import dataclass
from typing import Iterable, Protocol


@dataclass(frozen=True)
class RetrievedChunk:
    """A chunk of retrieved context."""

    content: str
    source: str
    score: float


class Retriever(Protocol):
    """Protocol for retrieval backends."""

    def retrieve(self, query: str, *, top_k: int) -> Iterable[RetrievedChunk]:
        """Return retrieved chunks for the given query."""
        raise NotImplementedError
