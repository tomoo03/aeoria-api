from ..api.dto.chatgpt import ChatGPTMessageModel
from pydantic import BaseModel
from typing import List

class AnalyzeDto(BaseModel):
    messages: List[dict[str, str]]
    source_lang: str = 'JA'
    text: str