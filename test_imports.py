from llama_index.core.schema import Document
from llama_index.readers.file import SimpleDirectoryReader

docs = SimpleDirectoryReader(input_dir="./documents").load_data()

for doc in docs:
    print(doc)
