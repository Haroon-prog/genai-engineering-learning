from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

question = 'what is Groq?'

response = llm.invoke(question)

print(response.content)