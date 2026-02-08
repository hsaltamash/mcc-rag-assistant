"""WhatsApp integration placeholder."""

from dataclasses import dataclass


@dataclass
class WhatsAppMessage:
    """Inbound WhatsApp message payload."""

    sender: str
    body: str


def handle_message(message: WhatsAppMessage) -> str:
    """Handle an inbound message."""
    return f"Received message from {message.sender}: {message.body}"
