from fastapi import APIRouter

from .fetch import get_session_id

v1 = APIRouter(prefix="/v1")


@v1.get("/session")
async def get_session():
    session_id = await get_session_id()
    return {"session_id": session_id}
