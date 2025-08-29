import os

from llama_index.core import VectorStoreIndex, Settings, StorageContext
from llama_index.core.schema import Document
from llama_index.readers.file import PyMuPDFReader
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
 


def get_index_from_text(text: str, model_name: str = "tinyllama"):
    splitter = TokenTextSplitter(separator=" ", chunk_size=512, chunk_overlap=50)
    chunks = splitter.split_text(text)

    documents = [Document(text=chunk) for chunk in chunks]

    llm = Ollama(model=model_name)
    embed_model = OllamaEmbedding(model_name=model_name)

    Settings.llm = llm
    Settings.embed_model = embed_model


    index = VectorStoreIndex.from_documents(documents)

    return index


if __name__ == "__main__":
    loader = PyMuPDFReader()
    documents = loader.load(file_path="./documents/jee_marksheet.pdf")

    text = documents[0].text

    index = get_index_from_text(text)

    index_dir = "./index"
    if not os.path.exists(index_dir):
        os.makedirs(index_dir)

    index.storage_context.persist(persist_dir=index_dir)

    print("✅ Index has been built and saved to ./index/")
