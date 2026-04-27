from fastapi import APIRouter
from api.routes.user import router as user_router
from api.routes.task import router as task_router
from api.routes.log import router as log_router

api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(task_router)
api_router.include_router(log_router)
