# zara/memory/session_memory.py
class SessionMemory:
    def __init__(self, limit=10):
        self.limit = limit
        self.messages = []

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.limit:
            self.messages = self.messages[-self.limit:]

    def get(self):
        return self.messages
