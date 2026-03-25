from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()


doc1 = Document(
    page_content="Virat Kohli is one of the most successful batsmen in modern cricket. Known for his aggressive batting style and consistency, he has scored thousands of runs across all formats. His passion and leadership have inspired millions of cricket fans.",
    metadata = {'team': "RCB"}
)
doc2 = Document(
    page_content="MS Dhoni is one of the greatest captains in cricket history and led India to multiple ICC trophies. Famous for his calm personality and finishing ability, he is also known for his lightning-fast wicket-keeping skills. Fans often call him “Captain Cool.”",
    metadata = {'team': "CSK"}
)
doc3 = Document(
    page_content="Rohit Sharma is a stylish opening batsman known for his elegant stroke play. He holds several records, including multiple double centuries in One Day Internationals. As a captain and batsman, he has been a major pillar of the Indian cricket team.",
    metadata = {'team': "MI"}
)
doc4 = Document(
    page_content="Jasprit Bumrah is one of the best fast bowlers in the world with a unique bowling action. He is especially famous for his deadly yorkers and ability to bowl under pressure. Bumrah has played a crucial role in many of Indias victories.",
    metadata = {'team': "MI"}
)
doc5 = Document(
    page_content="Ravindra Jadeja is a brilliant all-rounder who contributes with batting, bowling, and exceptional fielding. His quick left-arm spin bowling and powerful batting make him a key player for India. He is also known for his athletic fielding and sword-celebration.",
    metadata = {'team': "CSK"}
)

docs = [doc1,doc2,doc3,doc4,doc5]

# chroma vector store created
# vector_store = Chroma.from_documents(
#     embedding_function=GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview"),
#     persist_directory="my_chroma_db",
#     collection_name="sample",
#     documents=doc
# )

# vector_store.add_documents(docs)

# documents = vector_store.get()
# print(documents,end="\n\n\n")


result = vector_store.similarity_search_with_score(
    query="is virat kohli a batter?",
    k=1
)
print(result)


# result = vector_store.similarity_search_with_score(
#     query="who is the baller from them",
#     filter={'team' : 'MI'},
# )









#retrivers practice
retriever = vector_store.as_retriever(
    search_type='mmr',
    search_kwargs={'k': 3, 'lambda_mult': 0}
)
results = retriever.invoke("mention all the different batters from different teams?")

for i,doc in enumerate(results):
    print(f'\n----Results{i+1}------')
    print(doc.page_content)
# print(result)