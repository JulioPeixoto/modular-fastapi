from langchain_openai import ChatOpenAI

from src.core.settings import settings


class Chat:
    def __init__(self, model):
        self.model = model
        self._client = ChatOpenAI(model=model, api_key=settings.openai_api_key)

    @property
    def get_client(self):
        return self._client

    async def invoke(self, request: str) -> str:
        try:
            messages = [{"role": "user", "content": request}]
            response = await self._client.ainvoke(messages)
            return response.content
        except Exception as e:
            raise Exception(f"Error in Chat invoke: {str(e)}")
