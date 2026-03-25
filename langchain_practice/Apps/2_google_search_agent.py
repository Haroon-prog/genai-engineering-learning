from dotenv import load_dotenv
load_dotenv()

# google already has the tool integrated in the model itself so we dont need to define it separately like we did in basic agent
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0).bind_tools([{"google_search": {}}])



from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

memory = InMemorySaver()

agent = create_agent(
    model = llm,
    tools = [],
    checkpointer = memory,
    system_prompt = "You are a Google search agent. Always use the google_search tool to answer."
)

# question = "who is the new mayor of new york 2026?"

# response = agent.invoke({"messages": [{"role": "user", "content": question}]})

# print(response["messages"][-1].content)



while True:
    print(memory, end="\n\n")
    question = input("User: ")
    if question.lower() in ["exit", "quit", "q", "bye"]:
        print("Goodbye!", end="\n\n")
        break
    response = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
        {"configurable": {"thread_id": "110"}}
        )
    print("Agent: " ,response["messages"][-1].content , end="\n\n")