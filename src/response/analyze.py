from ..api.dto.chatgpt import ChatGPTMessageModel
from pydantic import BaseModel
from typing import List

class _Score(BaseModel):
    neg: float
    neu: float
    pos: float
    compound: float

class AnalyzeResponse(BaseModel):
    messages: List[ChatGPTMessageModel]
    score: _Score
