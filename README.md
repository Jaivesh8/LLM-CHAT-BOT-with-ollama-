# 🦙 Healthcare Document-aware Chatbot

This project is a **document-aware chatbot** powered by **TinyLlama** and **LLaMA-2** models via the Hugging Face Inference API.  
It allows users to upload healthcare policy documents and ask natural language questions. The chatbot retrieves relevant content from the documents and generates context-aware answers.

---

## 🚀 Features
- Extracts and processes text from PDF documents.
- Splits text into chunks and creates **semantic embeddings** using `BAAI/bge-small-en-v1.5`.
- Performs **cosine similarity search** to find the most relevant section.
- Generates context-aware answers using **TinyLlama** / **LLaMA-2**.
- Flask API endpoint (`/ask`) for chatbot interaction.

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **NLP/AI:** Hugging Face Inference API  
- **Embeddings:** `BAAI/bge-small-en-v1.5`  
- **LLM Models:** `TinyLlama/TinyLlama-1.1B-Chat-v1.0`, `meta-llama/Llama-2-7b-chat-hf`  
- **Utilities:** NumPy, PyPDF2, dotenv  

---

## 📂 Project Structure
.
├── app.py # Flask backend API
├── utils.py # Utility functions (embeddings, similarity, etc.)
├── documents/ # Folder containing PDF documents
│ └── sample_policy.pdf
├── requirements.txt # Python dependencies
├── .env.example # Example environment variables file
├── .gitignore # Ignore venv, .env, pycache, etc.
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Configure environment variables
Create a .env file in the root folder and add:

env
Copy code
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
▶️ Run the Application
bash
Copy code
python app.py
Flask will start at http://127.0.0.1:5000/.

📬 Usage
Send a POST request to /ask with your query:

bash
Copy code
curl -X POST http://127.0.0.1:5000/ask \
     -H "Content-Type: application/json" \
     -d '{"query": "What is the claim process in the health policy?"}'
Example Response:

json
Copy code
{
  "response": "To file a claim, submit hospital bills, discharge summary, and ID proof..."
}
📌 Future Improvements
Multi-document support.

Web UI for direct user interaction.

Vector database integration (FAISS / Pinecone).

Larger models for better reasoning.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📜 License
This project is licensed under the MIT License.

markdown
Copy code

---

