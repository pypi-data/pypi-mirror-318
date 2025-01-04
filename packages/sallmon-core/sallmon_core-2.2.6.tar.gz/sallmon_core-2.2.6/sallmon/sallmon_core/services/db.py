import sqlite3
import json

DB_FILE = "messages.db"

def init_db():
    """Initialize the database and create the messages table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id TEXT PRIMARY KEY,
            timestamp TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(message):
    """Save a message to the database if it's unique."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute("""
            INSERT INTO messages (id, timestamp, content)
            VALUES (?, ?, ?)
        """, (message["id"], message["timestamp"], json.dumps(message["content"])))
        conn.commit()
    except sqlite3.IntegrityError:
        # Ignore duplicate messages
        pass
    finally:
        conn.close()

def get_messages():
    """Retrieve all messages from the database."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, timestamp, content FROM messages")
    rows = c.fetchall()
    conn.close()
    return [{"id": row[0], "timestamp": row[1], "content": json.loads(row[2])} for row in rows]

# Initialize the database at startup
init_db()
