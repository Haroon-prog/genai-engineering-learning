from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  
import streamlit as st


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5)

st.title("🤖 AskBuddy- AI QnA bot")
st.markdown("QnA bot using google gemini model,streamlit and langchain")
query = st.chat_input("Ask me anything...")


if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages :
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)
    
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)

    response = llm.invoke(query)
    st.session_state.messages.append({"role": "ai", "content": response.content})
    st.chat_message("ai").markdown(response.content)











