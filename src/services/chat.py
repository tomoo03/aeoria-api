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

        # chat送信時、messageの先頭にsystemプロンプトを加える
        messages.insert(0, self.__create_message(CHAT_GPT_CONSTANT.SYSTEM_PROMPT['STANDARD_MODE'], CHAT_GPT_CONSTANT.ROLE['SYSTEM']))

        # user入力テキストを履歴として格納する
        messages.append(self.__create_message(dto['text'], CHAT_GPT_CONSTANT.ROLE['USER']))

        # 入力テキストをChatGPTに送信する
        chat_response = self.__chatGPTApi.chat(messages)

        # systemプロンプトを取り除く
        messages.pop(0)

        return ChatResponseGenerator(generator=chat_response, messages=messages).to_dict()

    def get_communication_message(self, dto: ChatDto):
        print(dto['messages'])
        genre = 'ジャンル：アニメ'
        messages: List[dict[str, str]] = dto['messages']

        # chat送信時、messageの先頭にsystemプロンプトとジャンルを加える
        messages.insert(0, self.__create_message(CHAT_GPT_CONSTANT.SYSTEM_PROMPT['COMMUNICATION_MODE'], CHAT_GPT_CONSTANT.ROLE['SYSTEM']))
        messages.insert(1, self.__create_message(genre, CHAT_GPT_CONSTANT.ROLE['USER']))

        # userメッセージが存在しない場合は、会話ジャンルを加える


        # user入力テキストを履歴として格納する
        messages.append(self.__create_message(dto['text'], CHAT_GPT_CONSTANT.ROLE['USER']))

        # 入力テキストをChatGPTに送信する
        chat_response = self.__chatGPTApi.chat(messages)

        # systemプロンプトとジャンルを取り除く
        messages.pop(0)
        messages.pop(0)

        return ChatResponseGenerator(generator=chat_response, messages=messages).to_dict()

    def __create_message(self, content: str, role: str) -> dict:
        return ChatGPTMessageModel(content=content, role=role).dict()