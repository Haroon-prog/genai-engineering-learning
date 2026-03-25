# Basic Agent with knowing how to build and use tools
from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool

@tool
def add_numbers(a: int, b: int) :
    """
    It will add two numbers and return the result.

    Args:
        a : Number one
        b : Number two
    """
    return a + b

@tool
def multiply_numbers(a: int, b: int) :
    """
    It will multiply two numbers and return the result.

    Args:
        a : Number one
        b : Number two
    """
    return a * b

# result = add.invoke({"a": 5, "b": 10})
# print(result)

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")



# Now we have tools and models , we just need to connect both for an agent to work

from langchain.agents import create_agent

agent = create_agent(
    model = llm,
    tools = [add_numbers, multiply_numbers],
    system_prompt = " You are a math teacher , and always use the tools to calculate ."
)

response = agent.invoke({"messages": [{"role":"user", "content": " what is the 2 + 30 * 10?"}]})

# for res in response["messages"]:
#     print(res)
#     print("\n")     this loop will give the complete convo in which it does (think, action(toolcall) observe & final answer)

print(response["messages"][-1].content) # this will give the final answer only


