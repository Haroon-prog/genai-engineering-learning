from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite") 



#1st prompt --> detailed report 
template1 = PromptTemplate(
    template = "Write a detailed report on {topic}",
    input_variables = ['topic']
)

#2nd prompt --> SUMMARY  
template2 = PromptTemplate(
    template = "Write a 5 line summary for the following text \n {text}",
    input_variables = ['text']
)


parser = StrOutputParser()


#sequential chain
chain = template1 | model | parser | template2 | model | parser   

result = chain.invoke({'topic': 'Black hole'})

print(result)

chain.get_graph().print_ascii()


# prompt_1 = template1.invoke({'topic': 'black hole '})

# result = model.invoke(prompt_1)

# prompt_2 = template2.invoke({'text': result.content})

# result = model.invoke(prompt_2)

# print(result.content)