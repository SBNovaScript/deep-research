from fastapi import APIRouter, WebSocket
from uuid import uuid4
from ..models.research import ResearchRequest, ResearchResponse

router = APIRouter()

@router.post("/api/research", response_model=ResearchResponse)
async def start_research(request: ResearchRequest) -> ResearchResponse:
    task_id = str(uuid4())
    # A real implementation would launch asynchronous processing here
    return ResearchResponse(id=task_id)

@router.get("/api/research/{task_id}", response_model=ResearchResponse)
async def get_research(task_id: str) -> ResearchResponse:
    # Placeholder result until real processing is added
    return ResearchResponse(id=task_id, result=None)

@router.websocket("/ws/research/{task_id}")
async def research_ws(websocket: WebSocket, task_id: str):
    await websocket.accept()
    await websocket.send_json({"id": task_id, "message": "Streaming not implemented"})
    await websocket.close()
