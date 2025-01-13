from fastapi import APIRouter

from src.api.tasks import router as task_router

web_router = APIRouter()

web_router.include_router(task_router)
