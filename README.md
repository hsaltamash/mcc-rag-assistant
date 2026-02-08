# MCC RAG Assistant

A production-leaning scaffold for a Retrieval-Augmented Generation (RAG) assistant built with
FastAPI, Chroma, and OpenAI.

## Structure

```
mcc-rag-assistant/
  app/
    __init__.py
    main.py
    core/
      __init__.py
      config.py
      logging.py
    rag/
      __init__.py
      chunking.py
      embeddings.py
      vector_store.py
      qa.py
      strength.py
    ingestion/
      __init__.py
      loaders.py
      ingest.py
    integrations/
      __init__.py
      whatsapp.py
    api/
      __init__.py
      routes_health.py
      routes_chat.py
      routes_admin_docs.py
  data/
    raw/
    extracted/
    chroma/
  docs/
    seed/
      parking.md
  scripts/
    run_dev.sh
  .env.example
  requirements.txt
  README.md
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# edit .env and paste OPENAI_API_KEY

python -c "from pathlib import Path; from app.ingestion.ingest import ingest_path; print(ingest_path(Path('docs/seed/parking.md')))"

bash scripts/run_dev.sh
```

### Test the API

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"If parking is full, where should I park and is there a shuttle?"}'
```
