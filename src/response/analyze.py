from pydantic import BaseModel

class AnalyzeResponse(BaseModel):
    neg: float
    neu: float
    pos: float
    compound: float