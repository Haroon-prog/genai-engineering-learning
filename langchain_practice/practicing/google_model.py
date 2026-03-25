from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7)
 

response = model.invoke("who is the new mayor of new york in 2026?")

print(response.content)        