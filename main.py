from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

MESSAGES_FILE = "messages.json"

# Load old messages
if not os.path.exists(MESSAGES_FILE):
    with open(MESSAGES_FILE, "w") as f:
        json.dump([], f)

@app.route("/")
def home():
    return "GhostLink Server Running"

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json(force=True)
    sender = data.get("sender", "Unknown")
    message = data.get("message", "")
    
    with open(MESSAGES_FILE, "r") as f:
        messages = json.load(f)
    messages.append({"sender": sender, "message": message})
    with open(MESSAGES_FILE, "w") as f:
        json.dump(messages, f)
    return jsonify({"status": "OK"})

@app.route("/messages", methods=["GET"])
def messages():
    with open(MESSAGES_FILE, "r") as f:
        messages = json.load(f)
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
