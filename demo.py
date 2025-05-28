import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]


from langchain_openai import OpenAI

llmModel = OpenAI()

for chunk in llmModel.stream(
    "Tell me one fun fact about Kennedy Family. I need detailed response"
):
    print(chunk, end = "", flush = True)