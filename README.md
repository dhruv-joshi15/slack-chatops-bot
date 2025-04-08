# Slack ChatOps Bot

A simple Python + Flask Slack bot that listens to `/deploy` and `/status` commands and responds with simulated DevOps automation messages.

## Commands
- `/status` – Returns a fake "all-systems-go" message.
- `/deploy` – Simulates a deployment trigger.

## Setup Instructions

1. Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file from the template:

```env
SLACK_VERIFICATION_TOKEN=your-token-here
```

3. Run the bot:

```bash
python app.py
```

4. Use a tool like [ngrok](https://ngrok.com/) to expose your local Flask server and set it as your Slack command URL.

## Example Usage

Send `/status` or `/deploy` in Slack and receive a simulated bot response.

✅ Built by Dhruv Joshi