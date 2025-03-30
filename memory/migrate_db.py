# memory/migrate_db.py

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "zara_memory.db")

def migrate():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        # Add is_fact column if it doesn't exist
        try:
            c.execute("ALTER TABLE conversations ADD COLUMN is_fact BOOLEAN DEFAULT 0")
            print("[Migration] 'is_fact' column added successfully.")
        except sqlite3.OperationalError as e:
            if "duplicate column name" in str(e):
                print("[Migration] 'is_fact' column already exists.")
            else:
                print(f"[Migration] Error: {e}")
        conn.commit()

if __name__ == "__main__":
    migrate()
