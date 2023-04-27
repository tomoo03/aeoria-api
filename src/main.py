from .routers import analyze, chat, transcriptions
from fastapi import FastAPI

app = FastAPI()
app.include_router(analyze.router)
app.include_router(chat.router)
app.include_router(transcriptions.router)