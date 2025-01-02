import logging
import os
import sqlite3
import json
from ..services.database import initialize_db

# Initialize the database and create tables if they don't exist
initialize_db()

logger = logging.getLogger("message_handler")

def get_db_connection():
    """Get a database connection."""
    db_path = os.path.expanduser("~/.sallmon/blockchain.db")
    conn = sqlite3.connect(db_path)
    return conn

def validate_json(data):
    """Validate that the data is valid JSON."""
    try:
        json.dumps(data)  # Try to serialize
        return True
    except (TypeError, ValueError):
        return False

def handle_transaction(content):
    """Process a transaction message."""
    required_fields = {"sender", "recipient", "amount"}
    if not required_fields.issubset(content):
        logger.error(f"Invalid transaction format: {content}")
        return {"type": "error", "content": "Invalid transaction format"}

    if not isinstance(content["amount"], (int, float)) or content["amount"] <= 0:
        logger.error(f"Invalid transaction amount: {content['amount']}")
        return {"type": "error", "content": "Invalid transaction amount"}

    logger.info(f"Valid transaction received: {content}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO transactions (sender, recipient, amount)
            VALUES (?, ?, ?)
        ''', (content["sender"], content["recipient"], content["amount"]))
        conn.commit()
        conn.close()
        logger.info("Transaction successfully saved.")
    except Exception as e:
        logger.error(f"Error saving transaction: {e}")
        return {"type": "error", "content": "Failed to save transaction"}

    return {"type": "response", "content": "Transaction received"}

def handle_block(content):
    """Process a block message."""
    required_fields = {"index", "previous_hash", "timestamp", "data", "hash"}

    if not required_fields.issubset(content):
        logger.error(f"Invalid block format: {content}")
        return {"type": "error", "content": "Invalid block format"}

    if not validate_json(content["data"]):
        logger.error(f"Block contains invalid JSON in data field: {content['data']}")
        return {"type": "error", "content": "Invalid JSON in block data"}

    logger.info(f"Block received: {content}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM blocks')
        block_count = cursor.fetchone()[0]

        if block_count == 0:
            content["previous_hash"] = "0"
            logger.info("Genesis block detected and will be added.")

        cursor.execute('''
            INSERT INTO blocks (block_index, previous_hash, timestamp, data, hash)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            content["index"],
            content["previous_hash"],
            content["timestamp"],
            json.dumps(content["data"]),  # Serialize data to valid JSON
            content["hash"]
        ))
        conn.commit()
        logger.info(f"Block successfully added: {content['hash']}")

        if block_count > 0 and content.get("data"):
            logger.info(f"Clearing {len(content['data'])} transactions from the mempool.")
            for txn in content["data"]:
                cursor.execute('''
                    DELETE FROM transactions
                    WHERE sender = ? AND recipient = ? AND amount = ?
                ''', (txn["sender"], txn["recipient"], txn["amount"]))
            conn.commit()
            logger.info("Transactions successfully cleared from the mempool.")
    except Exception as e:
        logger.error(f"Error processing block: {e}")
        return {"type": "error", "content": "Failed to process block"}
    finally:
        conn.close()

    return {"type": "response", "content": "Block added"}
