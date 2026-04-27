from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


class TaskIn(BaseModel):
    title: str


class TaskStatusIn(BaseModel):
    status: str


@router.post("")
def create_task(body: TaskIn):
    return TaskService.create_task(body.title)


@router.get("")
def list_tasks():
    return TaskService.list_tasks()


@router.patch("/{task_id}/status")
def update_task_status(task_id: int, body: TaskStatusIn):
    updated = TaskService.update_status(task_id, body.status)
    if not updated:
        raise HTTPException(status_code=404, detail="task not found")
    return updated
