"""Document chunking utilities."""

from typing import Iterable, List


def chunk_text(text: str, chunk_size: int = 500) -> List[str]:
    """Split text into fixed-size chunks."""
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


def chunk_collection(texts: Iterable[str], chunk_size: int = 500) -> List[str]:
    """Chunk a collection of texts into a flat list."""
    chunks: List[str] = []
    for text in texts:
        chunks.extend(chunk_text(text, chunk_size=chunk_size))
    return chunks
