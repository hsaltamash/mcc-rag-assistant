"""Question answering orchestration."""

from typing import List

from app.rag.chunking import chunk_text
from app.rag.embeddings import embed_texts
from app.rag.vector_store import build_records


def answer_question(question: str, context: str) -> str:
    """Generate a placeholder answer for a question."""
    chunks = chunk_text(context)
    embeddings = embed_texts(chunks)
    _records = build_records(chunks, embeddings)
    return f"Answering '{question}' with {len(chunks)} context chunks."
