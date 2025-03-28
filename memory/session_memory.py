# zara/memory/session_memory.py
class SessionMemory:
    def __init__(self):
        self.memory = []

    def remember(self, message: str):
        self.memory.append(message)

    def get_memory(self):
        return self.memory

    def clear(self):
        self.memory = []
