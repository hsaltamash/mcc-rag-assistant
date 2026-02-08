from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    app_name: str = "mcc-rag-assistant"
    environment: str = os.getenv("ENVIRONMENT", "dev")

    # OpenAI
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_chat_model: str = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
    openai_embed_model: str = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")

    # Vector store
    chroma_path: str = os.getenv("CHROMA_PATH", "./data/chroma")
    collection_name: str = os.getenv("CHROMA_COLLECTION", "mcc_kb")

    # RAG behavior
    top_k: int = int(os.getenv("TOP_K", "5"))
    min_similarity: float = float(os.getenv("MIN_SIMILARITY", "0.25"))  # tune later


settings = Settings()
