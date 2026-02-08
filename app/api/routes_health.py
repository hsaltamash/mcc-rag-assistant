"""Health check routes."""


def healthcheck() -> dict:
    """Return a simple health status payload."""
    return {"status": "ok"}
