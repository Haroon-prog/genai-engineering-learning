from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

# prompt = [
#     {"role": "user", "content": "hello myself Mir Haroon Ali"},
#     {"role": "ai", "content": "Hello Mir Haroon Ali! It's nice to meet you. How can I help you today?"},
#     {"role": "user", "content": "what is my name?"}

# ]

# result = llm.invoke(prompt)

# print(result.content)

#but above is not the STANDARD way 👆


# manage history in standard way 👇

print("memory QnA bot")
History = []

while True:
    query = input("User: ")
    History.append({"role": "user", "content": query})

    if query.lower() in ["exit", "quit", "bye", "q"]:
        print("Goodbye have a nice day!!!👋🙋‍♂️")
        break

    result = llm.invoke(History)
    History.append({"role": "ai", "content": result.content})
    print("AI: ",result.content , "\n")