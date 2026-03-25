from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser  # no need for response.content only print(response).
from dotenv import load_dotenv

load_dotenv()


def transform_case (text:str) :
    return text.upper()


out = StrOutputParser()  

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature = 0.5)

prompt = ChatPromptTemplate(
    [
        {"role":"system", "content" : "You are a {language} translator, and you wil translate the given english text in {language} "},
        {"role":"user", "content" : "{query}"},
    ]
)

# final_prompt = prompt.format_messages(language = "hinglish", query = "i love python & javascript"
# final_prompt =prompt.invoke({"language":"hinglish", "query": "i love langchain"}) 
# (prompt is also a runnable object we can invoke it directly by passing the required variables inform of dictionary)


# response = llm.invoke( prompt.invoke({"language":"hindi", "query": "i love langchain"})  )
# prompt -> llm -> response we can use chain to connect prompt and llm together and get the response in one line of code

chain = prompt | llm | out | transform_case
# prompt -> llm(prompt) -> out(llm) -> transform_case(out) -> response 

response = chain.invoke({"language":"hinglish", "query": " india is a very polluted country !"})
print(response)


#runnable : objects that can be run or invoke , they are used in sequencial chaining and builidng complex workflow using pipe '|'