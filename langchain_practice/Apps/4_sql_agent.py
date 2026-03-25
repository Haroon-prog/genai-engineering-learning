#db, llm , create_agent, tools, system prompt ,sreamlit

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
import streamlit as st




db = SQLDatabase.from_uri("sqlite:///my_tasks.db")

db.run("""
       
    CREATE TABLE IF NOT EXISTS tasks(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       title TEXT NOT NULL,
       description TEXT,
       status TEXT CHECK(status IN ('pending', 'in_progress', 'completed')) DEFAULT 'pending',
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       ); 


       """)
# print("db table  created successfully")

llm = ChatGroq(model="llama-3.1-8b-instant")


toolkit = SQLDatabaseToolkit(db=db, llm=llm) #takes two parameters db and llm
tools = toolkit.get_tools()


system_prompt = """
You are a task management assistant that interacts with a SQL database containing a 'tasks' table.  
TASK RULES:
1. Limit SELECT queries to 10 results max with ORDER BY created_at DESC
2. After CREATE/UPDATE/DELETE, confirm with SELECT query
3. If the user requests a list of tasks, present the output in a structured table format to ensure clean and organized display in the browser.

CRUD OPERATIONS:
    CREATE:INSERT INTO tasks (title, description, status)
    READ: SELECT * FROM tasks WHERE ... LIMIT 10
    UPDATE: UPDATE tasks SET status=? WHERE id=? OR title=?
    DELETE:DELETE FROM tasks WHERE id=? OR title=?

Table schema: id, title, description, status (pending/in_progress/completed), created_at.
"""

# for tool in tools:       # list of tools
#     print(tool.name)


#agent creation
@st.cache_resource    #so that agent should not get recall or recreate once the website is reloaded!
def get_agent():
    agent = create_agent(
        model = llm,
        tools = tools,
        checkpointer = InMemorySaver(),
        system_prompt = system_prompt,
    )
    return agent

agent = get_agent()

st.subheader("📃 Taskbot - Manage your Todo's ")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


question = st.chat_input("Manage you tasks ...")

if question:
    st.chat_message("user").markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})


    with st.chat_message("ai"):
        with st.spinner("Processing..."):
            response = agent.invoke(
                {"messages": [{"role": "user", "content": question}]},
                {"configurable": {"thread_id": "111"}}
            )
            result = response["messages"][-1].content
            st.markdown(result)
            st.session_state.messages.append({"role": "ai", "content": result})


