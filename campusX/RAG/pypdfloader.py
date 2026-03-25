from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dummy.pdf')

docs = loader.lazy_load()

for document in docs:
    print(document)
# print(len(docs))