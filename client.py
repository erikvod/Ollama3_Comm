import requests
import time

server_1 = "http://192.168.1.100:5000/chat"  # Replace with the first server's IP
server_2 = "http://192.168.1.101:5000/chat"  # Replace with the second server's IP

prompt_1 = "Michael Jackson starts the conversation about music."
prompt_2 = "Donald Trump responds with his thoughts on music and business."

# Start conversation
current_prompt = prompt_1
current_server = server_1
next_server = server_2

while True:
    response = requests.post(current_server, json={"model": "llama2", "message": current_prompt}).json()
    reply = response["response"]
    
    print(f"\n{current_server} AI: {reply}")

    # Swap servers and update prompt
    current_prompt = reply
    current_server, next_server = next_server, current_server

    time.sleep(2)  # Small delay for readability
