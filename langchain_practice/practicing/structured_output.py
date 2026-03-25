from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

text = "My name is Mir Haroon Ali and my email is mirharoonali143@gmail.com and my age is 21"

from pydantic import BaseModel,Field
from typing import List

# class ResponseStructure(BaseModel):
#     name:str = Field(description="Complete Name")
#     email:str = Field(description="Email Address")
#     age:int = Field(description="Age")


# structured_llm = llm.with_structured_output(ResponseStructure)

# result = structured_llm.invoke(f"please give me only name,email , and age from this {text}")

# print(result.model_dump())



class Movies(BaseModel):
    title:str = Field(description="Movie title")
    year:str = Field(description="Movie release year")


class AllMovies(BaseModel):
    movies:List[Movies]

Movies_llm = llm.with_structured_output(AllMovies)
result = Movies_llm.invoke("give me 3 recent trending movies ")

print(result)