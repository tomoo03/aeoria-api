from ..api.constants.chatGptConstant import CHAT_GPT_CONSTANT
from ..api.dto.chatgpt import  ChatGPTMessageModel
from ..api.services.chatgptApiService import ChatGPTApiService
from ..dto.chat import ChatDto
from ..response.chat import ChatResponseGenerator
from typing import List

class ChatService:
    def __init__(self):
        self.__chatGPTApi = ChatGPTApiService()

    def get_chat_message(self, dto: ChatDto):
        print(dto['messages'])
        messages: List[dict[str, str]] = dto['messages']

        # 初回のchat送信時のみ、systemプロンプトを加える
        if len(messages) == 0:
            messages.append(self.__create_message(CHAT_GPT_CONSTANT.SYSTEM_PROMPT, CHAT_GPT_CONSTANT.ROLE['SYSTEM']))

        # 入力テキストを履歴として格納する
        messages.append(self.__create_message(dto['text'], CHAT_GPT_CONSTANT.ROLE['USER']))

        # 入力テキストをChatGPTに送信する
        chat_response = self.__chatGPTApi.chat(messages)
        return ChatResponseGenerator(generator=chat_response, messages=messages).dict()

    def __create_message(self, content: str, role: str) -> dict:
        return ChatGPTMessageModel(content=content, role=role).dict()