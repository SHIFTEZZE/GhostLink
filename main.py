from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
messages = []

@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    messages.append({
        "sender": data.get("sender", "Unknown"),
        "text": data.get("text", ""),
        "time": datetime.now().strftime("%H:%M:%S")
    })
    return jsonify({"status": "sent"}), 200

@app.route("/receive", methods=["GET"])
def receive_messages():
    return jsonify(messages[-20:])  # last 20 messages

@app.route("/")
def home():
    return "<h2>GhostLink Server Active ⚡</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
