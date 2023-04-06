from fastapi import APIRouter
from ..dto.analyze import AnalyzeDto
from ..services.analyze import AnalyzeService

router = APIRouter()

@router.post("/analyze")
async def get_analyze(dto: AnalyzeDto):
    sentimentScore = await AnalyzeService().get_analyze(dto.text)
    return {"message": sentimentScore}