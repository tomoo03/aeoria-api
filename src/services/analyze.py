from ..api.dto.chatgpt import ChatGPTDto, ChatGPTMessageModel
from ..api.dto.deepl import DeeplTranslateDto
from ..api.services.chatgptApiService import ChatGPTApiService
from ..api.services.deeplApiService import DeeplApiService
from ..clients.vaderSentimentClient import VaderSentimentClient
from ..dto.analyze import AnalyzeDto
from ..response.analyze import AnalyzeResponse
from ..api.constants.chatGptConstant import CHAT_GPT_CONSTANT

class AnalyzeService:
    def __init__(self):
        self.__chatGPTApi = ChatGPTApiService()
        self.__deeplApi = DeeplApiService()
        self.__vaderSentimentClient = VaderSentimentClient()

    async def get_vaderSentiment_analyze(self, dto: AnalyzeDto) -> AnalyzeResponse:
        print(AnalyzeDto(messages=dto.messages, source_lang=dto.source_lang, text=dto.text))
        messages = dto.messages
        source_lang = dto.source_lang
        text = dto.text
        print('requestMessages')
        print(messages)

        # 初回のchat送信時のみ、systemプロンプトを加える
        if len(messages) == 0:
            systemMessageModel: ChatGPTMessageModel = {
                'content': CHAT_GPT_CONSTANT.SYSTEM_PROMPT,
                'role': CHAT_GPT_CONSTANT.ROLE['SYSTEM']
            }
            messages.append(systemMessageModel)

        messageModel: ChatGPTMessageModel = {
            'content': text,
            'role': CHAT_GPT_CONSTANT.ROLE['USER']
        }

        # 入力テキストを履歴として格納する
        messages.append(messageModel)

        # 入力テキストをChatGPTに送信する
        chatGPTDto: ChatGPTDto = {
            'messages': messages,
            'model': CHAT_GPT_CONSTANT.MODEL
        }
        print('hogehoge')
        chatGPTApiResponse = await self.__chatGPTApi.create(chatGPTDto)
        print('hugahuga')
        print(chatGPTApiResponse)
        messageModelFromChatGPT = chatGPTApiResponse['choices'][0]['message']

        # chatGPTから返却されたメッセージを履歴として格納する
        messages.append(messageModelFromChatGPT)

        # chatGPTから返却されたメッセージの英訳処理（入力が英語の場合は実行しない）
        analyzeTargetText: str = messageModelFromChatGPT['content']
        if source_lang != 'EN':
            deeplTranslateDtoFromInput: DeeplTranslateDto = {
                'source_lang': 'JA',
                'text': messageModelFromChatGPT['content'],
                'target_lang': 'EN'
            }
            translatedFromGPT = await self.__deeplApi.translate(deeplTranslateDtoFromInput)
            print('translatedFromGPT')
            print(translatedFromGPT)

            # 英訳結果テキストを代入
            analyzeTargetText: str = translatedFromGPT['translations'][0]['text']

        # ChatGPTからの応答を感情分析する
        sentimentScore = self.__vaderSentimentClient.printPolarityScores(analyzeTargetText)

        print('sentimentScore')
        print(sentimentScore)
        print('messages')
        print(messages)

        response: AnalyzeResponse = {
            'messages': messages,
            'score': sentimentScore
        }

        return response