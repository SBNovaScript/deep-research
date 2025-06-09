import asyncio
import logging
from dataclasses import dataclass, field
from typing import Dict, Optional, Any, List

from .crawler import WebCrawler
from .ai_connectors import OpenAIConnector
from .summarizer import Summarizer
from .citation_manager import CitationManager
from .report_generator import ReportGenerator
from .validator import Validator
from .search_planner import SearchPlanner
from .google_search import GoogleSearch


@dataclass
class ResearchTask:
    topic: str
    queue: asyncio.Queue = field(default_factory=asyncio.Queue)
    result: Optional[str] = None

tasks: Dict[str, ResearchTask] = {}
async_tasks: Dict[str, asyncio.Task] = {}

logger = logging.getLogger(__name__)

async def _generate_queries(task: ResearchTask, planner: SearchPlanner) -> List[str]:
    logger.info("Generating search queries for topic '%s'", task.topic)
    queries = await planner.generate(task.topic)
    logger.debug("Generated queries: %s", queries)
    for q in queries:
        await task.queue.put({"type": "thinking", "text": q})
    return queries


async def _collect_urls(task: ResearchTask, searcher: GoogleSearch, queries: List[str]) -> List[str]:
    logger.info("Collecting URLs for %d queries", len(queries))
    urls = await searcher.search_all(queries)
    logger.debug("Collected URLs: %s", urls)
    for url in urls:
        await task.queue.put({"type": "search", "url": url})
    return urls


async def _summarize_pages(
    task_id: str,
    task: ResearchTask,
    crawler: WebCrawler,
    summarizer: Summarizer,
    validator: Validator,
    citation_mgr: CitationManager,
    urls: List[str],
) -> List[str]:
    logger.info("Crawling and summarizing %d URLs", len(urls))
    pages = await crawler.crawl(task_id, urls)
    summaries: List[str] = []
    for url, text in pages:
        citation_mgr.add(url, text)
        await task.queue.put({"type": "citation", "url": url})
        logger.debug("Summarizing %s", url)
        summary = await summarizer.summarize(text)
        fact_check = await validator.fact_check(summary)
        bias_check = await validator.bias_check(summary)
        combined = f"{summary}\n\nFact Check: {fact_check}\nBias Check: {bias_check}"
        summaries.append(combined)
        for item in (summary, fact_check, bias_check):
            await task.queue.put({"type": "thinking", "text": item})
    return summaries


async def _run(task_id: str) -> None:
    task = tasks[task_id]
    logger.info("Starting research task %s for topic '%s'", task_id, task.topic)
    await task.queue.put({"type": "thinking", "text": f"Starting research on '{task.topic}'"})

    crawler = WebCrawler()
    connector = OpenAIConnector()
    planner = SearchPlanner(connector)
    searcher = GoogleSearch()
    summarizer = Summarizer(connector)
    validator = Validator(connector)
    citation_mgr = CitationManager()

    queries = await _generate_queries(task, planner)
    urls = await _collect_urls(task, searcher, queries)
    summaries = await _summarize_pages(
        task_id, task, crawler, summarizer, validator, citation_mgr, urls
    )

    report_gen = ReportGenerator(citation_mgr)
    task.result = report_gen.generate(summaries)
    await task.queue.put({"type": "final", "text": task.result})
    await task.queue.put(None)

def start(task_id: str, topic: str) -> None:
    logger.info("Queueing new research task %s", task_id)
    tasks[task_id] = ResearchTask(topic=topic)
    async_tasks[task_id] = asyncio.create_task(_run(task_id))

def get_queue(task_id: str) -> Optional[asyncio.Queue]:
    task = tasks.get(task_id)
    if task:
        return task.queue
    logger.warning("Queue requested for unknown task %s", task_id)
    return None

def get_result(task_id: str) -> Optional[str]:
    task = tasks.get(task_id)
    if task:
        return task.result
    logger.warning("Result requested for unknown task %s", task_id)
    return None


async def shutdown() -> None:
    logger.info("Shutting down %d running tasks", len(async_tasks))
    for task in async_tasks.values():
        if not task.done():
            task.cancel()
    if async_tasks:
        await asyncio.gather(*async_tasks.values(), return_exceptions=True)
    async_tasks.clear()
    tasks.clear()
    logger.info("Shutdown complete")
