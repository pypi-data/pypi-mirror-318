import os
import sqlite3
import json

def initialize_db():
    # Get the user's home directory and define the database path
    db_path = os.path.expanduser("~/.sallmon/blockchain.db")

    # Create the database file if it doesn't exist
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            recipient TEXT NOT NULL,
            amount INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create the blocks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            block_index INTEGER NOT NULL,
            previous_hash TEXT NOT NULL,
            timestamp INTEGER NOT NULL,
            data TEXT,
            hash TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')


    # Create the peers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS peers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            peer_url TEXT NOT NULL UNIQUE,
            last_seen DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create the chat table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')


    # Check if the blocks table is empty and add the genesis block if needed
    cursor.execute('SELECT COUNT(*) FROM blocks')
    block_count = cursor.fetchone()[0]

    if block_count == 0:
        # Define the genesis block with a valid JSON data field
        genesis_block_data = json.dumps({
            "message": "Genesis Block - Static",
            "note": "This is the genesis block of the blockchain."
        })

        genesis_block = {
            "block_index": 0,
            "previous_hash": "0",
            "timestamp": 1704028800,  # Replace with your desired static timestamp
            "data": genesis_block_data,  # Use the JSON-encoded string
            "hash": "sallmon9f8a7c6e5d4b3a2f1a0c9e8d7b6a5f4c3b2a1f0",  # Replace with your desired static hash
        }
        cursor.execute('''
            INSERT INTO blocks (block_index, previous_hash, timestamp, data, hash)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            genesis_block["block_index"],
            genesis_block["previous_hash"],
            genesis_block["timestamp"],
            genesis_block["data"],
            genesis_block["hash"]
        ))
        conn.commit()
        print("Static genesis block created.")

    # Commit and close the connection
    conn.commit()
    conn.close()
