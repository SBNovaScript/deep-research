from __future__ import annotations

from .ai_connectors import AIConnector


class Summarizer:
    """Use an AIConnector to summarize text."""

    def __init__(self, connector: AIConnector):
        self.connector = connector

    async def summarize(self, text: str) -> str:
        prompt = f"Summarize the following text:\n{text[:500]}"
        return await self.connector.complete(prompt)
