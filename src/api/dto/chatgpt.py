from pydantic import BaseModel
from typing import List

class ChatGPTMessageModel(BaseModel):
    content: str
    role: str

class ChatGPTDto(BaseModel):
    messages: List[ChatGPTMessageModel]
    model: str