from ..api.constants.chatGptConstant import CHAT_GPT_CONSTANT
from ..api.dto.chatgpt import ChatGPTDto, ChatGPTMessageModel
from ..api.services.chatgptApiService import ChatGPTApiService
from ..dto.chat import ChatDto
from ..response.chat import ChatResponse
from typing import List

class ChatService:
    def __init__(self):
        self.__chatGPTApi = ChatGPTApiService()

    def get_chat_message(self, dto: ChatDto) -> List[ChatGPTMessageModel]:
        print(dto.messages)
        messages = dto.messages
        text = dto.text

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
        result = self.__chatGPTApi.chat(messages)
        print('test')
        resultMessageModel: ChatGPTMessageModel = ChatGPTMessageModel(
            content=result,
            role=CHAT_GPT_CONSTANT.ROLE['ASSISTANT']
        ).dict()
        print("test2")
        # chatGPTから返却されたメッセージを履歴として格納する
        messages.append(resultMessageModel)
        response: ChatResponse = ChatResponse(messages=messages).dict()
        return response