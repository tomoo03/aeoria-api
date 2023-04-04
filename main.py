from fastapi import FastAPI
from clients.vaderSentimentClient import VaderSentimentClient

app = FastAPI()


@app.get("/")
async def root():
    client = VaderSentimentClient()
    text = client.printPolarityScores("I'm so happy.")
    return {"message": text}