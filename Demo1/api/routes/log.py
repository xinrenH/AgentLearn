from fastapi import APIRouter
from pydantic import BaseModel
from app.services.log_service import LogService

router = APIRouter(prefix="/logs", tags=["logs"])


class LogIn(BaseModel):
    content: str


@router.post("")
def add_log(body: LogIn):
    return LogService.add_log(body.content)


@router.get("")
def list_logs():
    return LogService.list_logs()
