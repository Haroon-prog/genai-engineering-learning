from dotenv import load_dotenv
load_dotenv()

# from langchain_groq import ChatGroq
# llm = ChatGroq(model="llama-3.3-70b-versatile")
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0).bind_tools([{"google_search": {}}])


# from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import tool

# @tool
# def google_search(query: str) -> str:
#     """Search Google for real-time information."""
#     return search.run(query)

# search = GoogleSerperAPIWrapper()
# result = search.run("who won the women's world cup in 2025?")
# print(result)

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
# from langgraph.graph import StateGraph


memory = InMemorySaver()
agent = create_agent(
    model = llm,
    tools = [],
    checkpointer = memory,
    system_prompt = "You are a Google search agent. Always use the google_search tool to answer.",

)

print(memory)

# check_pointer = InMemorySaver()
# builder = StateGraph(...)
# graph = builder.compile(checkpointer=check_pointer)

question = "who is the new mayor of new york 2026?"

response = agent.invoke(
    {"messages": [{"role": "user", "content": question}]},
    {"configurable": {"thread_id": "101"}}
    )

print(response["messages"][-1].content)
