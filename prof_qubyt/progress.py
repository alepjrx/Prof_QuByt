import json
import os

PROGRESS_FILE = 'data/progress.json'

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return{}

def save_progress(progress):
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as file:
        json.dump(progress, file, indent=4)