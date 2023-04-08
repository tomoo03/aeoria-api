from ..api.dto.chatgpt import ChatGPTMessageModel
from pydantic import BaseModel

class AnalyzeDto(BaseModel):
    source_lang: str = 'JA'
    text: str