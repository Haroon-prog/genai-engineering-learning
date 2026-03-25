from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

code = """

# Parent class
class Animal:
    def eat(self):
        print("This animal eats food")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating object of Dog
d = Dog()

# Calling methods
d.eat()
d.bark()
"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 200,
    chunk_overlap = 0
)


chunks = splitter.split_text(code)
print(chunks[0])