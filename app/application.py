from fastapi import FastAPI

from .api.routers import v1 as v1_router
from .database.db_mysql import init_db


def register_app() -> FastAPI:
    _app: FastAPI = FastAPI(title="FastAPI with Tortoise ORM")

    _app.include_router(v1_router)
    init_db(_app)

    return _app


app = register_app()
