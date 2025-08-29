# test_embedder.py

from utils.pdf_loader import extract_text_from_pdf
from utils.embedder import get_index_from_text

# Load your document text
text = extract_text_from_pdf("documents/jee_marksheet.pdf")

# Generate vector index using local Ollama model
index = get_index_from_text(text)

# Now query the index
query_engine = index.as_query_engine()
response = query_engine.query("What is the candidate's roll number and name?")
print(response)
