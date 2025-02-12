import socket
import time

SERVER_HOST = "127.0.0.1"  # Change to the server's IP address
SERVER_PORT = 5000

def start_client():
    """Connect to the server and initiate conversation."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        
        initial_prompt = "Let's discuss the future of AI."
        client_socket.sendall(initial_prompt.encode())
        
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            print(f"AI says: {data}")
            time.sleep(1)  # Simulate processing time
            client_socket.sendall(data.encode())  # Send AI response back as the next prompt

if __name__ == "__main__":
    start_client()
