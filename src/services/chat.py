from ..api.constants.chatGptConstant import CHAT_GPT_CONSTANT
from ..api.dto.chatgpt import  ChatGPTMessageModel
from ..api.services.chatgptApiService import ChatGPTApiService
from ..dto.chat import ChatDto
from typing import List

class ChatService:
    def __init__(self):
        self.__chatGPTApi = ChatGPTApiService()

    def get_chat_message(self, dto: ChatDto):
        print(dto['messages'])
        messages: List[dict[str, str]] = dto['messages']
        text: str = dto['text']

        # 初回のchat送信時のみ、systemプロンプトを加える
        if len(messages) == 0:
            systemMessageModel: ChatGPTMessageModel = ChatGPTMessageModel(
                content=CHAT_GPT_CONSTANT.SYSTEM_PROMPT,
                role=CHAT_GPT_CONSTANT.ROLE['SYSTEM']
            ).dict()
            messages.append(systemMessageModel)

        messageModel: ChatGPTMessageModel = ChatGPTMessageModel(
            content=text,
            role=CHAT_GPT_CONSTANT.ROLE['USER']
        ).dict()

        # 入力テキストを履歴として格納する
        messages.append(messageModel)

        # 入力テキストをChatGPTに送信する
        chat_response = self.__chatGPTApi.chat(messages)
        return {
            'generator': chat_response,
            'messages': messages
        }