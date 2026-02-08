from pathlib import Path
from app.rag.chunking import chunk_text
from app.rag.embeddings import embed_texts
from app.rag.vector_store import get_collection


def ingest_path(path: Path):
    from app.ingestion.loaders import load_text_from_file

    col = get_collection()
    text = load_text_from_file(path)
    chunks = chunk_text(text)

    vectors = embed_texts(chunks)

    ids = [f"{path.name}-chunk-{i}" for i in range(len(chunks))]
    metas = [{"source": str(path), "chunk_index": i} for i in range(len(chunks))]

    col.add(ids=ids, documents=chunks, embeddings=vectors, metadatas=metas)

    return {"file": str(path), "chunks": len(chunks)}
