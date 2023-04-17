from ..dto.chat import ChatDto
from ..services.chat import ChatService
from ..api.dto.chatgpt import ChatGPTMessageModel
from ..api.constants.chatGptConstant import CHAT_GPT_CONSTANT
from typing import Any, Generator, List
from fastapi import APIRouter, WebSocket
import json

router = APIRouter()
delimiters = ['。', '！', '!', '？', '?', '\n']

@router.websocket("/chat")
async def get_chat_message(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        json_data: ChatDto = json.loads(data)
        print(json_data)
        result = ChatService().get_chat_message(json_data)
        generator: Generator[Any | list | dict, None, None] | Any | list | dict = result['generator']
        messages: List[ChatGPTMessageModel] = result['messages']
        sentence = ''
        full_text = ''
        message_index = 0
        for chunk in generator:
            text = chunk['choices'][0]['delta'].get('content')
            if (text != None):
                sentence += text # 文字を結合
                full_text += text
                if (text in delimiters): # 区切り文字の場合、クライアント側に一文を返却する。
                    print(sentence)
                    split_response = {
                        'status': 'success',
                        'message_category': 'split',
                        'message': sentence,
                        'message_index': message_index
                    }
                    await websocket.send_text(f"{split_response}")
                    sentence = ''
                    message_index += 1
            else:
                if (chunk['choices'][0].get('finish_reason') != None):
                    messages.append({
                        'role': CHAT_GPT_CONSTANT.ROLE['ASSISTANT'],
                        'content': full_text
                    })
                    finish_response = {
                        'status': 'success',
                        'message_category': 'finish',
                        'messages': messages,
                        'message_index': message_index
                    }
                    await websocket.send_text(f"{finish_response}")
