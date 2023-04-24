from ..constants.chat import ChatConstant
from ..dto.chat import ChatDto
from ..services.chat import ChatService
from ..api.dto.chatgpt import ChatGPTMessageModel
from ..api.constants.chatGptConstant import CHAT_GPT_CONSTANT
from typing import Any, Generator, List
from fastapi import APIRouter, Depends, WebSocket
import json

router = APIRouter()
delimiters = ['。', '！', '!', '？', '?', '\n'] # あとで正規表現に直す

# テキストチャットAPI
@router.websocket("/chat")
async def get_chat_message(websocket: WebSocket, chatService: ChatService = Depends(ChatService)):
    await websocket.accept()

    async def send_response(category: str, **kwargs):
        response = {'status': ChatConstant.RESPONSE_STATUS['SUCCESS'], 'message_category': category, **kwargs}
        await websocket.send_text(f"{response}")

    while True:
        data = await websocket.receive_text()
        print(data)
        json_data: ChatDto = json.loads(data)
        print(json_data)
        result = chatService.get_chat_message(json_data)
        generator: Generator[Any | list | dict, None, None]
        messages: List[ChatGPTMessageModel]
        generator, messages = result['generator'], result['messages']
        sentence, full_text, message_index = '', '', 0

        for chunk in generator:
            text = chunk['choices'][0]['delta'].get('content')

            if not text:
                if chunk['choices'][0].get('finish_reason'):
                    messages.append({
                        'role': CHAT_GPT_CONSTANT.ROLE['ASSISTANT'],
                        'content': full_text
                    })
                    await send_response(ChatConstant.MESSAGE_CATEGORY['FINISH'], messages=messages, message_index=message_index)
                continue

            sentence += text # 文字を結合
            full_text += text

            if text in delimiters: # 区切り文字の場合、クライアント側に一文を返却する。
                await send_response(ChatConstant.MESSAGE_CATEGORY['SPLIT'], message=sentence, message_index=message_index)
                sentence, message_index = '', message_index + 1
