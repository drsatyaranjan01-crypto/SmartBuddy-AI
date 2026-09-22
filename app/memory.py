import json
import os


MEMORY_FILE = "data/memory.json"


def load_memory():
    """Load SmartBuddy's saved memory."""

    if not os.path.exists(MEMORY_FILE):
        return {
            "user": {},
            "facts": [],
            "preferences": [],
            "goals": []
        }

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(memory):
    """Save memory to memory.json."""

    os.makedirs("data", exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            memory,
            file,
            indent=4,
            ensure_ascii=False
        )


def remember(category, value):
    """Add something to SmartBuddy's memory."""

    memory = load_memory()

    if category == "name":
        memory["user"]["name"] = value

    elif category in ["facts", "preferences", "goals"]:
        if value not in memory[category]:
            memory[category].append(value)

    save_memory(memory)


def get_memory():
    """Return all saved memory."""

    return load_memory()