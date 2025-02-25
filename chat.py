import ollama
import json

# Define the personas
persona_1 = "Michael Jackson"
persona_2 = "Donald Trump"

# Initial system prompt
system_prompt = f"Michael Jackson and Donald Trump are having a conversation. Michael is friendly and passionate about music, while Trump is bold and opinionated."

# Function to chat with a model
def chat_with_model(model_name, prompt):
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Start the conversation
print("Welcome to AI Chat! Type 'exit' to quit.")
history = []

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'exit':
        break

    # Michael Jackson responds
    mj_response = chat_with_model('llama2', f"{system_prompt}\n{persona_1}: {user_input}")
    history.append(f"{persona_1}: {mj_response}")
    print(f"\n{persona_1}: {mj_response}")

    # Donald Trump responds
    trump_response = chat_with_model('llama2', f"{system_prompt}\n{persona_2}: {mj_response}")
    history.append(f"{persona_2}: {trump_response}")
    print(f"\n{persona_2}: {trump_response}")
