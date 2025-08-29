from utils.ollama_client import ask_ollama

print("Welcome to your local chatbot! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    reply = ask_ollama(user_input)
    print("Bot:", reply)


