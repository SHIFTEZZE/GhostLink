from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
messages = []

# Send message endpoint
@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400
    messages.append({
        "sender": data.get("sender", "Unknown"),
        "text": data.get("text", ""),
        "time": datetime.now().strftime("%H:%M:%S")
    })
    return jsonify({"status": "sent"}), 200

# Receive messages endpoint
@app.route("/receive", methods=["GET"])
def receive_messages():
    # Return last 20 messages
    return jsonify(messages[-20:])

# Simple homepage to pass health checks
@app.route("/")
def home():
    return "<h2>GhostLink Server Active ⚡</h2>"

# Start the server on Koyeb-friendly host and port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
