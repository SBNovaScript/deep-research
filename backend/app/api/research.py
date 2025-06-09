from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from uuid import uuid4
from ..models.research import ResearchRequest, ResearchResponse
from ..services import research_runner

router = APIRouter(prefix="/api", tags=["research"])

@router.post("/research", response_model=ResearchResponse)
async def start_research(request: ResearchRequest) -> ResearchResponse:
    task_id = str(uuid4())
    research_runner.start(task_id, request.topic)
    return ResearchResponse(id=task_id)

@router.get("/research/{task_id}", response_model=ResearchResponse)
async def get_research(task_id: str) -> ResearchResponse:
    result = research_runner.get_result(task_id)
    return ResearchResponse(id=task_id, result=result)

@router.websocket("/ws/research/{task_id}")
async def research_ws(websocket: WebSocket, task_id: str):
    await websocket.accept()
    queue = research_runner.get_queue(task_id)
    if not queue:
        await websocket.send_json({"message": "Invalid task"})
        await websocket.close()
        return
    try:
        while True:
            message = await queue.get()
            if message is None:
                break
            await websocket.send_json(message)
    except WebSocketDisconnect:
        pass
    finally:
        await websocket.close()
