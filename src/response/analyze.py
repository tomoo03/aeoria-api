from pydantic import BaseModel

class _Score(BaseModel):
    neg: float
    neu: float
    pos: float
    compound: float

class AnalyzeResponse(BaseModel):
    score: _Score
    text: str
