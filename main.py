from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simple in-memory store
messages = []

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    sender = data.get('sender', 'Unknown')  # default if missing
    text = data.get('text', '')
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    msg = {
        'sender': sender,
        'text': text,
        'time': timestamp
    }
    messages.append(msg)
    return jsonify({'status': 'ok'}), 200

@app.route('/receive', methods=['GET'])
def receive_messages():
    return jsonify(messages), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
