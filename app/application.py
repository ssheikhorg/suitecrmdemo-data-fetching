from fastapi import FastAPI

from .api.routers import v1 as v1_router


app = FastAPI()

app.include_router(v1_router)
