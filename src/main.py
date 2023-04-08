from .routers import analyze
from fastapi import FastAPI

app = FastAPI()
app.include_router(analyze.router)