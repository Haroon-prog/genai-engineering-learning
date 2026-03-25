from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts  import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda


# from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

groq_model =ChatGroq(model="llama-3.1-8b-instant")
parser = StrOutputParser()

class classifier (BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description=" Give the sentiment of the following feedback either positive or negative in one word")

parser2 = PydanticOutputParser(pydantic_object= classifier)

prompt1 = PromptTemplate(
    template=" Classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)



prompt2 = PromptTemplate(
    template=" Write an appropriate Response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template=" Write an appropriate Response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

classifier_chain = prompt1 | groq_model | parser2

# print(type(classifier_chain.invoke({'feedback':"this device is excellent !"})))

branchchain = RunnableBranch(
    (lambda x:x.sentiment == 'positive' , prompt2 | groq_model | parser),
    (lambda x:x.sentiment == 'negative' , prompt3 | groq_model | parser),
    RunnableLambda(lambda x: " could not find the sentiment!")
)

chain = classifier_chain | branchchain

result = chain.invoke({'feedback':"this device is excellent !"})

print(result,end="\n\n")

chain.get_graph().print_ascii()

