import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Default Ollama endpoint
MODEL_NAME = "mistral"  # Change to the model you want to use

def send_message(prompt, context=""):
    """Send a message to the Ollama AI and receive a response."""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "context": context
    }
    
    response = requests.post(OLLAMA_API_URL, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("response"), data.get("context")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None, None

def chat():
    """Allow a human to chat with the AI while maintaining context."""
    context = ""
    print("Start chatting with the AI. Type 'exit' to stop.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response, context = send_message(user_input, context)
        if response:
            print(f"AI: {response}")

if __name__ == "__main__":
    chat()
