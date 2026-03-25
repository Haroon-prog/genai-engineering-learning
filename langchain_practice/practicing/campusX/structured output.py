from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7) 

#schema
class Review (TypedDict):
    summary : Annotated[str,"A brief summary of review "]
    sentiment : Annotated[str , "return sentiment of the review either positive , negative or neutral"]
    pros : Annotated[Optional[list[str]],"write down all the pros inside a list "]
    cons : Annotated[Optional[list[str]],"write down all the cons   inside a list "]

structured_model = model.with_structured_output(Review)


response = structured_model.invoke("""
The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
                        """)

print(response)
# print(response["summary"])  

