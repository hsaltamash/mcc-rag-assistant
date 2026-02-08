import chromadb
from app.core.config import settings


def get_collection():
    client = chromadb.PersistentClient(path=settings.chroma_path)
    return client.get_or_create_collection(name=settings.collection_name)
