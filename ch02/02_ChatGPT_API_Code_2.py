import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "너는 친절하게 답변해주는 비서야"},
        {"role": "user", "content": "2019년 월드시리즈에서는 누가 우승했어?"},
    ],
)
print(response["choices"][0]["message"]["content"])
