from __future__ import annotations
from typing import Any
import os
import logging

from openai import AsyncOpenAI


class AIConnector:
    """Base class for AI service connectors."""

    async def complete(self, prompt: str) -> str:
        raise NotImplementedError


class EchoConnector(AIConnector):
    """Simple connector that echoes the prompt."""

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    async def complete(self, prompt: str) -> str:
        self.logger.debug("EchoConnector returning prompt")
        return f"Echo: {prompt}"


class OpenAIConnector(AIConnector):
    """Connector for the OpenAI API using the asynchronous client."""

    def __init__(self, api_key: str | None = None, model: str = "gpt-3.5-turbo") -> None:
        self.client = AsyncOpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.logger = logging.getLogger(__name__)

    async def complete(self, prompt: str) -> str:
        self.logger.debug("Sending completion request")
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        result = response.choices[0].message.content
        self.logger.debug("Received completion response")
        return result
