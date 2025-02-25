from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    model_name = data.get('model', 'llama2')
    message = data.get('message', '')

    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": message}])
    return jsonify({"response": response['message']['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
