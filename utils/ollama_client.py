# utils/ollama_client.py
import requests
from ollama import Client

client = Client(host="http://127.0.0.1:11434", timeout=120)


def ask_ollama(prompt, model="mistral"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json()["response"]
