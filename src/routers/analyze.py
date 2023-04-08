from ..dto.analyze import AnalyzeDto
from ..response.analyze import AnalyzeResponse
from ..services.analyze import AnalyzeService
from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
async def get_analyze(dto: AnalyzeDto) -> AnalyzeResponse:
    print(dto)
    response = await AnalyzeService().get_vaderSentiment_analyze(dto)
    return response