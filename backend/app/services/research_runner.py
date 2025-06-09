import asyncio
from dataclasses import dataclass, field
from typing import Dict, Optional, Any


@dataclass
class ResearchTask:
    topic: str
    queue: asyncio.Queue = field(default_factory=asyncio.Queue)
    result: Optional[str] = None

tasks: Dict[str, ResearchTask] = {}


async def _run(task_id: str) -> None:
    task = tasks[task_id]
    await task.queue.put({"message": f"Starting research on '{task.topic}'"})
    for i in range(1, 4):
        await asyncio.sleep(0.1)
        await task.queue.put({"message": f"Processing step {i} for '{task.topic}'"})
    task.result = f"Summary for {task.topic}"
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
