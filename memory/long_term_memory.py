# memory/long_term_memory.py

import sqlite3
from datetime import datetime

class LongTermMemory:
    def __init__(self, db_path="memory/long_term_memory.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role TEXT,
                    content TEXT,
                    timestamp TEXT
                )
            """)

    def store(self, role, content):
        with self.conn:
            self.conn.execute(
                "INSERT INTO memory (role, content, timestamp) VALUES (?, ?, ?)",
                (role, content, datetime.utcnow().isoformat())
            )

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT role, content, timestamp FROM memory ORDER BY id DESC")
        return cursor.fetchall()
