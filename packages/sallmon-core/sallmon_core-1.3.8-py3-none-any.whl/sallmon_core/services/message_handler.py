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

from pydantic import BaseModel, ValidationError

# Define ChatMessage class
class ChatMessage(BaseModel):
    sender: str
    message: str

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

def handle_command(content):
    """Process an admin command message."""
    action = content.get("action")
    params = content.get("params", {})

    if not action:
        logger.error("Invalid command: Missing action field.")
        return {"type": "error", "content": "Missing action field in command"}

    if action == "broadcast_message":
        message = params.get("message")
        if not message:
            return {"type": "error", "content": "Missing 'message' in broadcast command"}
        logger.info(f"Broadcasting message to all peers: {message}")
        # Implement broadcasting logic here
        return {"type": "response", "content": f"Broadcast message: {message}"}

    elif action == "sync_peers":
        logger.info("Forcing peer synchronization.")
        # Implement logic to re-sync peers
        return {"type": "response", "content": "Peer synchronization triggered"}

    elif action == "update_config":
        logger.info(f"Updating configuration with params: {params}")
        # Implement configuration update logic here
        return {"type": "response", "content": "Configuration updated"}

    else:
        logger.warning(f"Unknown admin command action: {action}")
        return {"type": "error", "content": "Unknown admin command action"}

# Chat handler
def handle_chat(content):
    """Process a chat message."""
    try:
        chat_message = ChatMessage(**content)
    except ValidationError as e:
        logger.error(f"Chat message validation error: {e}")
        return {"type": "error", "content": "Invalid chat message format"}

    logger.info(f"Chat message received from {chat_message.sender}: {chat_message.message}")
    # Broadcast chat message to all peers
    asyncio.create_task(broadcast_chat_message(chat_message))
    return {"type": "response", "content": "Chat message received"}

async def broadcast_chat_message(chat_message: ChatMessage):
    """Broadcast a chat message to all peers."""
    message = {
        "type": "chat",
        "content": {
            "sender": chat_message.sender,
            "message": chat_message.message
        }
    }
    logger.info(f"Broadcasting chat message: {message}")
    await broadcast_message_to_peers(message)
