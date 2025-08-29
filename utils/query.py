# utils/query.py

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
import os

def main():
    index_dir = "./index"
    if not os.path.exists(index_dir):
        print("❌ Index directory not found. Run embedder.py first.")
        return

   
    llm = Ollama(model="llama2")
    embed_model = OllamaEmbedding(model_name="llama2")

    storage_context = StorageContext.from_defaults(persist_dir=index_dir)
    index = load_index_from_storage(
        storage_context,
        embed_model=embed_model  
    )

    query_engine = index.as_query_engine(llm=llm)

    while True:
        query = input("\nAsk a question (or type 'exit' to quit): ")
        if query.lower() in ["exit", "quit"]:
            break

        response = query_engine.query(query)
        print("\n🧠 Answer:", response)

if __name__ == "__main__":
    main()
