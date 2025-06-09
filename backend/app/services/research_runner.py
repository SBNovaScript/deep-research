import asyncio
from dataclasses import dataclass, field
from typing import Dict, Optional, Any, List

from .crawler import WebCrawler
from .ai_connectors import OpenAIConnector
from .summarizer import Summarizer
from .citation_manager import CitationManager
from .report_generator import ReportGenerator
from .validator import Validator


@dataclass
class ResearchTask:
    topic: str
    queue: asyncio.Queue = field(default_factory=asyncio.Queue)
    result: Optional[str] = None

tasks: Dict[str, ResearchTask] = {}


async def _run(task_id: str) -> None:
    task = tasks[task_id]
    await task.queue.put({"message": f"Starting research on '{task.topic}'"})

    crawler = WebCrawler()
    connector = OpenAIConnector()
    summarizer = Summarizer(connector)
    validator = Validator(connector)
    citation_mgr = CitationManager()

    urls = ["https://example.com"]
    pages = await crawler.crawl(task_id, urls)
    summaries: List[str] = []
    for url, text in pages:
        citation_mgr.add(url, text)
        summary = await summarizer.summarize(text)
        fact_check = await validator.fact_check(summary)
        bias_check = await validator.bias_check(summary)
        combined = f"{summary}\n\nFact Check: {fact_check}\nBias Check: {bias_check}"
        summaries.append(combined)
        await task.queue.put({"message": summary})
        await task.queue.put({"message": fact_check})
        await task.queue.put({"message": bias_check})

    report_gen = ReportGenerator(citation_mgr)
    task.result = report_gen.generate(summaries)
    await task.queue.put({"message": task.result})
    await task.queue.put(None)

def start(task_id: str, topic: str) -> None:
    tasks[task_id] = ResearchTask(topic=topic)
    asyncio.create_task(_run(task_id))

def get_queue(task_id: str) -> Optional[asyncio.Queue]:
    task = tasks.get(task_id)
    if task:
        return task.queue
    return None

def get_result(task_id: str) -> Optional[str]:
    task = tasks.get(task_id)
    return task.result if task else None
