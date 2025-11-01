from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
messages = []

@app.route('/send', methods=['POST'])
def send():
    sender = request.form.get('sender')
    text = request.form.get('text')
    timestamp = datetime.now().strftime("%H:%M:%S")
    if sender and text:
        messages.append({'sender': sender, 'text': text, 'time': timestamp})
        return "Message sent."
    return "Missing data.", 400

@app.route('/receive', methods=['GET'])
def receive():
    return jsonify(messages[-10:])

@app.route('/')
def home():
    return "GhostLink Server Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
