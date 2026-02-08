# MCC RAG Assistant

A scaffolded layout for a Retrieval-Augmented Generation (RAG) assistant. This repository is organized
around a modular `app/` package with ingestion, RAG, integrations, and API route stubs.

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
python app/main.py
```
