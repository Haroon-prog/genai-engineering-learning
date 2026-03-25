from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature = 0.5 , streaming = True)

question ="what is genai ?"
streamed_response = llm.stream(question)

for chunk in streamed_response:
    print(chunk.content , end="")