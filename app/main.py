from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api.routes_health import router as health_router
from app.api.routes_chat import router as chat_router

log = setup_logging()

app = FastAPI(title="MCC RAG Assistant")

app.include_router(health_router)
app.include_router(chat_router)


@app.on_event("startup")
def on_startup():
    log.info("app_started")
