"""Chat routes."""

from app.rag.qa import answer_question
from app.rag.strength import score_strength


def chat(question: str, context: str) -> dict:
    """Answer a chat question using RAG."""
    answer = answer_question(question, context)
    strength = score_strength(answer)
    return {"answer": answer, "strength": strength}
