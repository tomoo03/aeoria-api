from ..api.constants.chatGptConstant import CHAT_GPT_CONSTANT
from ..api.dto.chatgpt import ChatGPTDto, ChatGPTMessageModel
from ..api.services.chatgptApiService import ChatGPTApiService
from ..dto.chat import ChatDto
from ..response.chat import ChatResponse

class ChatService:
    def __init__(self):
        self.__chatGPTApi = ChatGPTApiService()

    async def get_chat_message(self, dto: ChatDto) -> ChatResponse:
        messages = dto.messages
        text = dto.text

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
        chatGPTApiResponse = await self.__chatGPTApi.create(chatGPTDto)
        messageModelFromChatGPT = chatGPTApiResponse['choices'][0]['message']

        # chatGPTから返却されたメッセージを履歴として格納する
        messages.append(messageModelFromChatGPT)

        response: ChatResponse = {
            'messages': messages,
        }

        return response

    def chain(self, dto: ChatDto) -> str:
        print(dto.messages)
        result = self.__chatGPTApi.chain(dto.messages)
        return result