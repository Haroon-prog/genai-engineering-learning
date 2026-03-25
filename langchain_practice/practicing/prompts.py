from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm  = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)

prompt = [
    {"role":"system", "content" : "You are a hindi translator, and you wil translate the given english text in hindi "},
    {"role":"user", "content" : "i love langchain !"},
]

response = llm.invoke(prompt)

print(response.content)