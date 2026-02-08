from openai import OpenAI
from app.core.config import settings
from app.rag.embeddings import embed_texts
from app.rag.vector_store import get_collection

_client = OpenAI(api_key=settings.openai_api_key)

SYSTEM = (
    "You are a grounded assistant.\n"
    "Use ONLY the provided CONTEXT.\n"
    "If the answer is not in the context, say: 'Not found in the provided documents.'\n"
    "Cite sources like [1], [2]."
)


def answer_question(question: str, top_k: int | None = None) -> dict:
    col = get_collection()
    k = top_k or settings.top_k

    q_vec = embed_texts([question])[0]
    res = col.query(query_embeddings=[q_vec], n_results=k)

    docs = res["documents"][0] if res.get("documents") else []
    metas = res["metadatas"][0] if res.get("metadatas") else []
    distances = res["distances"][0] if res.get("distances") else []

    contexts = []
    for i, (d, m) in enumerate(zip(docs, metas), start=1):
        src = m.get("source", "unknown")
        contexts.append({"idx": i, "source": src, "text": d})

    context_block = "\n\n".join(
        [f"[{c['idx']}] Source: {c['source']}\n{c['text']}" for c in contexts]
    )

    user_msg = f"CONTEXT:\n{context_block}\n\nQUESTION:\n{question}"

    chat = _client.chat.completions.create(
        model=settings.openai_chat_model,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.2,
    )

    return {
        "answer": chat.choices[0].message.content,
        "sources": [{"source": c["source"], "idx": c["idx"]} for c in contexts],
        "distances": distances,
    }
