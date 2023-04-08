from .routers import analyze, chat
from fastapi import FastAPI

app = FastAPI()
app.include_router(analyze.router)
app.include_router(chat.router)