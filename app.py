import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SLACK_VERIFICATION_TOKEN = os.getenv("SLACK_VERIFICATION_TOKEN")

@app.route("/", methods=["GET"])
def index():
    return "Slack ChatOps Bot is running!"

@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.form
    token = data.get("token")
    command = data.get("command")
    user = data.get("user_name")

    if token != SLACK_VERIFICATION_TOKEN:
        return jsonify({"error": "Invalid token"}), 403

    if command == "/status":
        return f"Hi {user}, the latest deployment is stable. ✅"
    elif command == "/deploy":
        return f"Hi {user}, triggering deployment now... 🚀 (simulated)"
    else:
        return f"Hi {user}, unknown command. 🤖"

if __name__ == "__main__":
    app.run(debug=True)