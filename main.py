from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory store of messages
messages = []

# Send a message
@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json() or {}
    sender = data.get('sender', 'Unknown')        # default if missing
    text = data.get('text', '')                   # default empty string
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    msg = {
        'sender': sender,
        'text': text,
        'time': timestamp
    }
    messages.append(msg)
    return jsonify({'status': 'ok'}), 200

# Receive messages (universal endpoint)
@app.route('/receive', methods=['GET'])
@app.route('/messages', methods=['GET'])
def get_messages():
    # Always return full messages list
    return jsonify(messages), 200

# Health check (optional)
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'online'}), 200

if __name__ == '__main__':
    # Listen on all addresses and port 8080
    app.run(host='0.0.0.0', port=8080)
