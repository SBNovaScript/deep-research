from __future__ import annotations

from .ai_connectors import AIConnector
from ..prompts import SUMMARY_TEMPLATE


class Summarizer:
    """Use an AIConnector to summarize text."""

    def __init__(self, connector: AIConnector):
        self.connector = connector

    async def summarize(self, text: str) -> str:
        prompt = SUMMARY_TEMPLATE.format(text=text[:500])
        return await self.connector.complete(prompt)
