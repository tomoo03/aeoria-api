from ..dto.analyze import AnalyzeDto
from ..response.analyze import AnalyzeResponse
from ..services.analyze import AnalyzeService
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/analyze")
async def get_analyze(dto: AnalyzeDto, analyzeService: AnalyzeService = Depends(AnalyzeService)) -> AnalyzeResponse:
    print(dto)
    response = await analyzeService.get_vaderSentiment_analyze(dto)
    return response