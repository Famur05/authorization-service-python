from fastapi import FastAPI
from app.core.exceptions import register_exception_handlers
from app.routers import router

app = FastAPI()

register_exception_handlers(app)

app.include_router(router)
