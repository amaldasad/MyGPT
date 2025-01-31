from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Home route
@app.route('/')
def home():
    return render_template('chat.html')

# Route to handle chat messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Prepare the payload for Ollama
    payload = {
        "model": "deepseek-r1:1.5b",  # Use the deepseek-r1:1.5b model
        "prompt": user_message,
        "stream": False
    }
    
    # Send the request to Ollama
    response = requests.post(OLLAMA_API_URL, json=payload)
    
    if response.status_code == 200:
        bot_response = response.json().get('response')
        return jsonify({'message': "NorrisBro:"+bot_response})
    else:
        return jsonify({'message': 'Error: Unable to get response from Amal das.'}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)