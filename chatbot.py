import json
from ai_model import get_ai_response

MEMORY_FILE = "memory.json"

# 📂 Load memory
def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except:
        return []

# 💾 Save memory
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

# 🗑️ Clear memory
def clear_memory():
    save_memory([])
    return True

def get_response(user_input):
    text = user_input.lower()

    # 🔥 LOAD MEMORY
    memory = load_memory()

    # 🔥 GET AI RESPONSE USING MEMORY
    response = get_ai_response(memory[-3:], user_input)

    # 🔥 SAVE MEMORY (Limit to last 50 entries to optimize performance)
    memory.append({
        "user": user_input,
        "bot": response
    })

    save_memory(memory[-50:])

    return response