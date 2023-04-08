from ..dto.chatgpt import ChatGPTMessageModel
from pydantic import BaseModel
from typing import List

class Choice(BaseModel):
    finish_reason: str
    message: ChatGPTMessageModel
    index: int

class Usage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

class ChatGPTResponse(BaseModel):
    object: str
    choices: List[Choice]
    created: int
    id: str
    usage: Usage