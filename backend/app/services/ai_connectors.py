from __future__ import annotations
from typing import Any


class AIConnector:
    """Base class for AI service connectors."""

    async def complete(self, prompt: str) -> str:
        raise NotImplementedError


class EchoConnector(AIConnector):
    """Simple connector that echoes the prompt."""

    async def complete(self, prompt: str) -> str:
        return f"Echo: {prompt}"
