from __future__ import annotations
from typing import List

from .ai_connectors import AIConnector
from ..prompts import SEARCH_QUERY_TEMPLATE


class SearchPlanner:
    """Generate search queries for a research prompt using an AIConnector."""

    def __init__(self, connector: AIConnector, max_queries: int = 5) -> None:
        self.connector = connector
        self.max_queries = max_queries

    async def generate(self, prompt: str) -> List[str]:
        ai_prompt = SEARCH_QUERY_TEMPLATE.format(prompt=prompt, n=self.max_queries)
        response = await self.connector.complete(ai_prompt)
        queries: List[str] = []
        for line in response.splitlines():
            cleaned = line.strip().lstrip('-*0123456789. ').strip()
            if cleaned:
                queries.append(cleaned)
        return queries[: self.max_queries]
