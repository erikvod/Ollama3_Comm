import socket
import requests
import json

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 5000
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

def generate_response(prompt, context=""):
    """Generate AI response using Ollama."""
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
        return "Error generating response", ""

def start_server():
    """Start a server to receive messages and respond."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            context = ""
            
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                
                print(f"Received: {data}")
                response, context = generate_response(data, context)
                print(f"AI Responds: {response}")
                
                conn.sendall(response.encode())

if __name__ == "__main__":
    start_server()
