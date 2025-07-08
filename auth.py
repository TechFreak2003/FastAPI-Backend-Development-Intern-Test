import secrets
import json
import os
from typing import Optional, Dict
from datetime import datetime

HISTORY_FILE = "history.json"

USERS = {
    "alice": "password123",
    "bob": "secret"
}

active_tokens: Dict[str, str] = {}  # token -> username


def load_history() -> dict:
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return {}


def save_history(history: dict):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def authenticate_user(username: str, password: str) -> Optional[str]:
    if username in USERS and USERS[username] == password:
        token = secrets.token_urlsafe(32)
        active_tokens[token] = username

        # Initialize user history in file if not exists
        history = load_history()
        if username not in history:
            history[username] = []
            save_history(history)

        return token
    return None


def get_current_user(token: str) -> Optional[str]:
    return active_tokens.get(token)


def add_prompt_to_history(username: str, prompt: str, response: str):
    timestamp = datetime.now().isoformat()
    history = load_history()

    if username not in history:
        history[username] = []

    history[username].append({
        "timestamp": timestamp,
        "prompt": prompt,
        "response": response
    })

    save_history(history)


def get_user_history(username: str) -> list:
    history = load_history()
    return history.get(username, [])
