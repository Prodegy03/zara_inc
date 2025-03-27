import json
import os
from datetime import datetime

class Memory:
    def __init__(self, memory_file='volumes/memory/zara_memory.json'):
        self.memory_file = memory_file
        self.data = {
            "log": [],
            "requests": []
        }

    def load(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = {"log": [], "requests": []}
        else:
            self.save()

    def save(self):
        os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
        with open(self.memory_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def log_task(self, task, result):
        self.data["log"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "task": task,
            "result": result
        })
        self.save()

    def store_request(self, request):
        self.data["requests"].append({
            "timestamp": datetime.utcnow().isoformat(),
            "description": request.get("description", "Unnamed"),
            "type": request.get("type", "general"),
            "payload": request.get("payload", {})
        })
        self.save()

    def retrieve_latest_request(self):
        if self.data["requests"]:
            return self.data["requests"].pop(0)
        return None
