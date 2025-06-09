import asyncio
from dataclasses import dataclass, field
from typing import Dict, Optional, Any, List

from .crawler import WebCrawler
from .ai_connectors import EchoConnector
from .summarizer import Summarizer
from .citation_manager import CitationManager
from .report_generator import ReportGenerator


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
    connector = EchoConnector()
    summarizer = Summarizer(connector)
    citation_mgr = CitationManager()

    urls = ["https://example.com"]
    pages = await crawler.crawl(task_id, urls)
    summaries: List[str] = []
    for url, text in pages:
        citation_mgr.add(url, text)
        summary = await summarizer.summarize(text)
        summaries.append(summary)
        await task.queue.put({"message": summary})

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
