from pydantic import BaseModel

class AnalyzeDto(BaseModel):
    source_lang: str = 'EN'
    text: str
    target_lang: str = 'JA'