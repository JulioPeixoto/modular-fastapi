# functions.py

from langchain_openai import ChatOpenAI 
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def openai_request(prompt_text: str) -> str:
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("API key not found in environment variables")

        model = ChatOpenAI(
            model="gpt-3.5-turbo", 
            api_key=api_key
        )

        messages = [{"role": "user", "content": prompt_text}]

        response = model(messages=messages)

        return response.content

    except Exception as e:
        raise Exception(f"Error in OpenAI request: {str(e)}")  # Converte a exceção em string para serialização
