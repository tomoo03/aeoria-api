from pydantic import BaseModel

class AnalyzeDto(BaseModel):
    text: str