import sqlite3
import os

DB_PATH = os.path.join("memory", "zara_memory.db")

def reset_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("[Memory Reset] Old memory database deleted.")
    else:
        print("[Memory Reset] No existing memory database found.")

    # Recreate the database and table
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("[Memory Reset] New memory database created with fresh table.")

if __name__ == "__main__":
    reset_database()
