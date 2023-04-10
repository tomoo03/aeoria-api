from ..api.dto.deepl import DeeplTranslateDto
from ..api.services.deeplApiService import DeeplApiService
from ..clients.vaderSentimentClient import VaderSentimentClient
from ..dto.analyze import AnalyzeDto
from ..response.analyze import AnalyzeResponse

class AnalyzeService:
    def __init__(self):
        self.__deeplApi = DeeplApiService()
        self.__vaderSentimentClient = VaderSentimentClient()

    async def get_vaderSentiment_analyze(self, dto: AnalyzeDto) -> AnalyzeResponse:
        source_lang = dto.source_lang
        text = dto.text

        # メッセージの英訳処理（入力が英語の場合は実行しない）
        analyzeTargetText: str = text
        if source_lang != 'EN':
            deeplTranslateDto: DeeplTranslateDto = DeeplTranslateDto(
                source_lang=source_lang,
                text=text,
                target_lang='EN'
            ).dict()
            translatedText = await self.__deeplApi.translate(deeplTranslateDto)
            print(translatedText)

            # 英訳結果テキストを代入
            analyzeTargetText: str = translatedText

        # テキストを感情分析する
        sentimentScore = self.__vaderSentimentClient.printPolarityScores(analyzeTargetText)

        response: AnalyzeResponse = AnalyzeResponse(
            neg=sentimentScore['neg'],
            neu=sentimentScore['neu'],
            pos=sentimentScore['pos'],
            compound=sentimentScore['compound']
        )

        return response