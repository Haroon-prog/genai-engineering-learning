#llm , agent, google search tool, memory saver, streaming , streamlit (web interface)


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# memory and history (to print complete convo )
if "memory" not in st.session_state:
    st.session_state.memory = InMemorySaver()
    st.session_state.history = []
    

#llm and google search tool 
llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite",streaming = True, temperature=0).bind_tools([{"google_search": {}}])

#agent 
agent = create_agent(
            model = llm,
            tools = [],
            checkpointer = st.session_state.memory,
            system_prompt = "You are a Google search agent . Always use the google search tool to answer users queries."
        )


#web interface with streamlit
st.subheader("🤖 QnA Google Search Chatbot")

question = st.chat_input("Ask me anything...")

# print the complete convo as msgs are appended in history list .
for msg in st.session_state.history:
    role = msg["role"]
    content = msg["content"]
    st.chat_message(role).markdown(content)


if question:
    st.chat_message("user").markdown(question)
    st.session_state.history.append({"role": "user", "content": question})

    response = agent.stream(
        {"messages": [{"role": "user", "content" : question}]},
        {"configurable" : {"thread_id" : "110"}},
        stream_mode = "messages"
        )
    
    # for streamed response  
    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty()

        message = ""

        for chunk in response:
            message = message + chunk[0].content
            space.markdown(message)

        st.session_state.history.append({"role": "ai", "content": message})    







