from memory.session_memory import SessionMemory
from memory import long_term_memory

class MemoryManager:
    def __init__(self, short_term_limit=10):
        self.session = SessionMemory(limit=short_term_limit)
        self.long_term = long_term_memory

    def add(self, role, content):
        self.session.add(role, content)
        self.long_term.store_message(role, content)

    def get_recent(self):
        return self.session.get()

    def get_long_term(self, limit=10):
        return self.long_term.retrieve_recent_messages(limit=limit)
