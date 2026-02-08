# MCC RAG Assistant

A minimal Python project scaffold for a Retrieval-Augmented Generation (RAG) assistant. This starter repo includes:

- A simple configuration model.
- A placeholder retrieval interface.
- A tiny CLI entrypoint.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[cli]"

mcc-rag-assistant --help
```

## Project layout

```
.
├── pyproject.toml
├── README.md
└── src/
    └── mcc_rag_assistant/
        ├── __init__.py
        ├── cli.py
        ├── config.py
        └── retrieval.py
```
