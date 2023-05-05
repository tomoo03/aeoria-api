from pydantic import BaseModel

class AnalyzeDto(BaseModel):
    source_lang: str = 'JA'
    text: str