from openai import OpenAI
from app.core.config import settings

_client = OpenAI(api_key=settings.openai_api_key)


def embed_texts(texts: list[str]) -> list[list[float]]:
    resp = _client.embeddings.create(
        model=settings.openai_embed_model,
        input=texts,
    )
    return [d.embedding for d in resp.data]
