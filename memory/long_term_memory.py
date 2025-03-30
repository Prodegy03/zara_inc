# memory/long_term_memory.py

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "zara_memory.db")

# Create or update the conversations table
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                is_fact BOOLEAN DEFAULT 0
            )
        ''')
        conn.commit()

# Store a message with optional fact flag
def store_message(role, content, is_fact=False):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO conversations (role, content, is_fact)
            VALUES (?, ?, ?)
        ''', (role, content, int(is_fact)))
        conn.commit()

# Find a matching fact or fallback to recent assistant message
def find_similar_or_recent(user_input):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        # Search for a matching fact (basic string containment search for now)
        c.execute('''
            SELECT content FROM conversations
            WHERE is_fact = 1 AND content LIKE ?
            ORDER BY timestamp DESC LIMIT 1
        ''', (f"%{user_input}%",))
        row = c.fetchone()
        if row:
            return row[0]

        # Fallback: get most recent assistant message
        c.execute('''
            SELECT content FROM conversations
            WHERE role = 'assistant'
            ORDER BY timestamp DESC LIMIT 1
        ''')
        row = c.fetchone()
        return row[0] if row else None

init_db()
