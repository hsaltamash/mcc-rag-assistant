"""Ingestion pipeline orchestration."""

from pathlib import Path

from app.ingestion.loaders import load_markdown_dir
from app.rag.chunking import chunk_collection
from app.rag.embeddings import embed_texts
from app.rag.vector_store import build_records


def ingest_seed_docs(seed_dir: Path) -> int:
    """Ingest markdown documents from a seed directory."""
    documents = load_markdown_dir(seed_dir)
    chunks = chunk_collection(documents)
    embeddings = embed_texts(chunks)
    _records = build_records(chunks, embeddings)
    return len(_records)
