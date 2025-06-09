from __future__ import annotations
from typing import Any
import os

from openai import AsyncOpenAI


class AIConnector:
    """Base class for AI service connectors."""

    async def complete(self, prompt: str) -> str:
        raise NotImplementedError


class EchoConnector(AIConnector):
    """Simple connector that echoes the prompt."""

    async def complete(self, prompt: str) -> str:
        return f"Echo: {prompt}"


class OpenAIConnector(AIConnector):
    """Connector for the OpenAI API using the asynchronous client."""

    def __init__(self, api_key: str | None = None, model: str = "gpt-3.5-turbo") -> None:
        self.client = AsyncOpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model

    async def complete(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
