from ..dto.chat import ChatDto
from ..response.chat import ChatResponse
from ..services.chat import ChatService
from ..api.dto.chatgpt import ChatGPTMessageModel
from ..api.constants.chatGptConstant import CHAT_GPT_CONSTANT
from typing import Any, Generator, List
from fastapi import APIRouter, WebSocket
import openai
import json

router = APIRouter()
delimiters = ['。', '！', '!', '？', '?', '\n']

def test_get_chat_message(dto: ChatDto):
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
    chat_response = chat(messages)
    return {
        'generator': chat_response,
        'messages': messages
    }
        # yield ChatGPTMessageModel(
        #     content=f"{chunk['choices'][0]['delta'].get('content')}",
        #     role=CHAT_GPT_CONSTANT.ROLE['ASSISTANT']
        # ).dict()

def chat(messages: List[ChatGPTMessageModel]):
    return openai.ChatCompletion.create(
        frequency_penalty=0.5,
        max_tokens=1024,
        messages=messages,
        model="gpt-3.5-turbo",
        n=1,
        presence_penalty=0.5,
        stop=None,
        stream=True,
        temperature=0.5,
    )

    # sentence = ''
    # target_char = ['。', '！', '？', '\n']
    # async for chunk in streamData:
    #     finishReason = chunk['choices'][0]['delta'].get('finish_reason')
    #     content: str = chunk['choices'][0]['delta'].get('content')

    #     if (finishReason == None and content == None):
    #         pass
    #     elif (finishReason == None and content != None):
    #         if (content in target_char):
    #             sentence += content
    #             yield sentence
    #             sentence = ''
    #         else:
    #             sentence += content
    #             print(content, end='', flush=True)
    #     else:
    #         for message in messages:
    #             yield message['content']

@router.websocket("/chat")
async def get_chat_message(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        json_data: ChatDto = json.loads(data)
        print(json_data)
        result = test_get_chat_message(json_data)
        generator: Generator[Any | list | dict, None, None] | Any | list | dict = result['generator']
        messages: List[ChatGPTMessageModel] = result['messages']
        sentence = ''
        full_text = ''
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
                        'message': sentence
                    }
                    await websocket.send_text(f"{split_response}")
                    sentence = ''
            else:
                if (chunk['choices'][0].get('finish_reason') != None):
                    messages.append({
                        'role': CHAT_GPT_CONSTANT.ROLE['ASSISTANT'],
                        'content': full_text
                    })
                    finish_response = {
                        'status': 'success',
                        'message_category': 'finish',
                        'messages': messages
                    }
                    await websocket.send_text(f"{finish_response}")

    # def event_stream():
    #     for chunk in result:
    #         print(chunk['choices'][0]['delta'].get('content'))
    #         # ここには、「はい！」のような文字列がきてほしい
    #         yield f"data: {chunk}\n\n"

    # response_lines = call_chatgpt_api()

    # async def event_stream():
    #     async for line in response_lines:
    #         await asyncio.sleep(1)
    #         yield f"data: {line}\n\n"
    # return StreamingResponse(event_stream(), media_type="text/event-stream")