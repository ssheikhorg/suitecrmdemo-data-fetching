from fastapi import APIRouter

from .fetch import get_session_id

v1 = APIRouter(prefix="/v1")


@v1.get("/fetch-data")
async def get_session() -> dict:
    return await get_session_id()
