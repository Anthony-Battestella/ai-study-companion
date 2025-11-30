import json
import os

def load_user(name):
    filename = f"{name.lower()}_profile.json"
    
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)

    return {"name": name, "level": "Beginner", "quizzes": 0}

def save_user(user):
    filename = f"{user['name'].lower()}_profile.json"
    with open(filename, "w") as f:
        json.dump(user, f, indent=4)
