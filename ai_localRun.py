import ollama
import time

# Define the personas
persona_1 = "Michael Jackson"
persona_2 = "Robin Williams"

# System prompt to guide the conversation
system_prompt = """Michael Jackson and Robin Williams are having a conversation. 
They respond in character and stay true to their personalities.
"""

# Function to interact with the model
def chat_with_model(model_name, persona, message):
    prompt = f"{system_prompt}\n{persona}: {message}\n"
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Initial conversation starter
message = "Hey Michael, what do you think about the world today?"
turn = 0

while True:
    # Determine who is speaking
    current_persona = persona_1 if turn % 2 == 0 else persona_2

    # Get response
    response = chat_with_model("artifish/llama3.2-uncensored", current_persona, message)

    # Print the conversation
    print(f"\n\n{current_persona}: {response}")

    # Check for clear command
    if response.lower() == "clear":
        print("\nChat history cleared. Restarting conversation...")
        message = "Hey Michael, what do you think about the world today?"
        turn = 0
        continue

    # Pass the response as the next message
    message = response
    turn += 1

    # Pause for readability
    time.sleep(2)
