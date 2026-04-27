from fastapi import APIRouter
from pydantic import BaseModel
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


class UserIn(BaseModel):
    name: str


@router.post("")
def create_user(body: UserIn):
    return UserService.create_user(body.name)


@router.get("")
def list_users():
    return UserService.list_users()
