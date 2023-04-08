from ..clients.httpxClient import HttpxClient
from ..constants.apiRequestConstant import API_REQUEST_CONSTANT
from ..constants.chatGptConstant import CHAT_GPT_CONSTANT
from ..dto.chatgpt import ChatGPTDto
from ..response.chatgpt import ChatGPTResponse
from typing import Any
import config
from langchain.llms import OpenAIChat
from langchain import PromptTemplate, LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class ChatGPTApiService:
    __API_KEY: str = config.OPENAI_API_KEY
    __COMPLETION_URL: str = API_REQUEST_CONSTANT.OPENAI['COMPLETION_URL']

    def __init__(self):
        self.__httpClient = HttpxClient()

    async def create(self, dto: ChatGPTDto) -> (Any | ChatGPTResponse):
        headers = {
            API_REQUEST_CONSTANT.AUTHORIZATION: f"{API_REQUEST_CONSTANT.OPENAI['SCHEME']['AUTHORIZATION']} {self.__API_KEY}",
        }
        body = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "こんにちは"}]
        }
        response: ChatGPTResponse = await self.__httpClient.json_post(self.__COMPLETION_URL, dto, headers)
        return response

    def chain(self, text: str) -> str:
        messages = [
            SystemMessage(content=CHAT_GPT_CONSTANT.SYSTEM_PROMPT),
            HumanMessage(content=text),
            AIMessage(content="ツン子っていうのよ"),
            HumanMessage(content="なにそれ変な名前"),
            AIMessage(content="なにそれひどい"),
            HumanMessage(content="ごめんごめん")
        ]
        chat = ChatOpenAI(model_name="gpt-3.5-turbo")
        result = chat(messages).content
        return result
        # LLMの準備
        # prefix_messages = [
        #     {"role": "system", "content": CHAT_GPT_CONSTANT.SYSTEM_PROMPT}
        # ]
        # llm = OpenAIChat(
        #     model_name="gpt-3.5-turbo",
        #     prefix_messages=prefix_messages
        # )

        # # プロンプトテンプレートの準備
        # template = """Q: {question}

        # A: """
        # prompt = PromptTemplate(
        #     template=template,
        #     input_variables=["question"]
        # )

        # # チェーンの準備
        # llm_chain = LLMChain(
        #     prompt=prompt,
        #     llm=llm
        # )

        # # チェーンの実行
        # question = text
        # result = llm_chain.run(question)
        # print("result")

        # system_settings = CHAT_GPT_CONSTANT.SYSTEM_PROMPT
        # prompt = ChatPromptTemplate.from_messages([
        #     SystemMessagePromptTemplate.from_template(system_settings),
        #     MessagesPlaceholder(variable_name="history"),
        #     HumanMessagePromptTemplate.from_template("{input}")
        # ])
        # memory = ConversationBufferMemory(return_messages=True)

        # conversation = ConversationChain(
        #     memory=memory,
        #     prompt=prompt,
        #     llm=ChatOpenAI(model_name="gpt-3.5-turbo"))
        # print(memory.load_memory_variables({}))
        # resp = conversation.predict(input=text)
        # return resp

        # system_settings = CHAT_GPT_CONSTANT.SYSTEM_PROM
        # prompt = ChatPromptTemplate.from_messages([
        #     SystemMessagePromptTemplate.from_template(system_settings),
        #     MessagesPlaceholder(variable_name="history"),
        #     HumanMessagePromptTemplate.from_template("{input}")
        # ])
        # conversation = ConversationChain(
        #     memory=ConversationBufferMemory(return_messages=True),
        #     prompt=prompt,
        #     llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))
        # conversation.predict(input="こんにちは")
        # conversation.predict(input="お腹すいた")

        # return result