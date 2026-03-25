from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts  import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

google_model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

groq_model = ChatGroq(model = "llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template=" Generate five questions and answers from the following text  \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template=" Merge the provided notes and quiz into the single document  \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | google_model | parser,
    'quiz' : prompt2 | groq_model | parser
})

merge_chain = prompt3 | groq_model | parser

chain = parallel_chain | merge_chain

text = """
**Generative Artificial Intelligence (GenAI)** is a branch of artificial intelligence that focuses on creating new content such as text, images, audio, video, and code by learning patterns from large datasets. Unlike traditional AI systems that mainly analyze or classify existing data, GenAI models are designed to generate original outputs that resemble human-created content. These systems are typically built using advanced machine learning techniques such as deep learning and neural networks, especially architectures like **transformers** and **large language models (LLMs)**. Popular examples include tools like ChatGPT, Gemini, and DALL·E. GenAI works by training on massive datasets containing text, images, or other media, allowing the model to understand patterns, context, and relationships within the data. When given a prompt, the model predicts and generates the most suitable output based on its learned knowledge. This technology is widely used in applications such as automated content creation, chatbots, coding assistants, design generation, drug discovery, and personalized education. Businesses and developers are increasingly integrating GenAI into products to improve productivity, creativity, and decision-making. However, despite its powerful capabilities, GenAI also raises important challenges related to accuracy, bias, ethical use, and misinformation, making responsible development and regulation essential for its safe and beneficial use in society.

"""

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()