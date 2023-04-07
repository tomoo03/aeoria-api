from ..clients.vaderSentimentClient import VaderSentimentClient
from ..dto.analyze import AnalyzeDto
from ..response.analyze import AnalyzeResponse
from ..api.services.deeplApiService import DeeplApiService
from ..api.dto.deepl import DeeplTranslateDto

class AnalyzeService:
    deeplApi: DeeplApiService
    vaderSentimentClient: VaderSentimentClient

    def __init__(self):
        self.deeplApi = DeeplApiService()
        self.vaderSentimentClient = VaderSentimentClient()

    async def get_vaderSentiment_analyze(self, dto: AnalyzeDto) -> AnalyzeResponse:
        # 入力テキストの英訳処理
        dtoFromInput: DeeplTranslateDto = {
            'source_lang': dto.source_lang,
            'text': dto.text,
            'target_lang': dto.target_lang
        }
        translatedDto = await self.deeplApi.translate(dtoFromInput)
        print('translatedDto')
        print(translatedDto)

        translatedMessageFromInput: str = translatedDto['translations'][0]['text']

        # 英訳済みテキストをChatGPTに送信する

        # ChatGPTからの応答を日本語に翻訳する（非同期実行）
        dtoFromGPT: DeeplTranslateDto = {
            'source_lang': 'EN',
            'text': translatedMessageFromInput,
            'target_lang': 'JA'
        }
        translatedDtoFromGPT = self.deeplApi.translate(dtoFromGPT)

        # ChatGPTからの応答を感情分析する（非同期実行）
        sentimentScore = self.vaderSentimentClient.printPolarityScores(translatedMessageFromInput)

        # 非同期処理の終了を待つ
        resolved = await translatedDtoFromGPT
        print('sentimentScore')
        print(sentimentScore)
        print('resolved')
        print(resolved)

        response: AnalyzeResponse = {
            'text': resolved['translations'][0]['text'],
            'score': sentimentScore
        }

        return response