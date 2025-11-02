from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS  # <-- add this

app = Flask(__name__)
CORS(app)  # <-- enable CORS

messages = []

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

@app.route("/receive", methods=["GET"])
def receive_messages():
    return jsonify(messages[-20:])

@app.route("/")
def home():
    return "<h2>GhostLink Server Active ⚡</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
