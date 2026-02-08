from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.qa import answer_question

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(req: ChatRequest):
    return answer_question(req.question)
