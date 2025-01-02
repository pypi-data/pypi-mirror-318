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
    """📦 Process a block message (with warnings for invalid cases)."""
    print("🛠️ [Dev Warning] Processing block... Check logs for details.")
    logger.debug(f"🛠️ Processing block: {content}")

    required_fields = {"index", "previous_hash", "timestamp", "data", "hash"}

    # Validate block structure
    if not required_fields.issubset(content):
        missing_fields = required_fields - content.keys()
        warning_msg = f"⚠️ [Dev Warning] Invalid block format. Missing fields: {missing_fields}. Block: {content}"
        print(warning_msg)
        logger.warning(warning_msg)
        return {"type": "warning", "content": f"Invalid block format. Missing fields: {missing_fields}"}

    # Validate JSON in the data field
    if not validate_json(content["data"]):
        warning_msg = f"⚠️ [Dev Warning] Block contains invalid JSON in data field. 🛑 Data: {content['data']}"
        print(warning_msg)
        logger.warning(warning_msg)
        return {"type": "warning", "content": "Invalid JSON in block data"}

    # Validate block index and hash integrity
    if content["index"] < 0:
        warning_msg = f"⚠️ [Dev Warning] Invalid block index: {content['index']}. Expected non-negative integer."
        print(warning_msg)
        logger.warning(warning_msg)
        return {"type": "warning", "content": "Invalid block index"}

    if not isinstance(content["hash"], str) or len(content["hash"]) == 0:
        warning_msg = f"⚠️ [Dev Warning] Invalid block hash: {content['hash']}. Expected non-empty string."
        print(warning_msg)
        logger.warning(warning_msg)
        return {"type": "warning", "content": "Invalid block hash"}

    print("🔍 [Dev Info] Validating block. Check logs for details.")
    logger.info(f"🔍 Validating block: {content}")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Validate previous hash consistency
        cursor.execute('SELECT hash FROM blocks WHERE block_index = ?', (content["index"] - 1,))
        previous_hash = cursor.fetchone()
        if content["index"] > 0 and (not previous_hash or previous_hash[0] != content["previous_hash"]):
            warning_msg = (
                f"⚠️ [Dev Warning] Previous hash mismatch. 🟡 Provided: {content['previous_hash']}, "
                f"🔵 Expected: {previous_hash[0] if previous_hash else 'None'}"
            )
            print(warning_msg)
            logger.warning(warning_msg)
            return {"type": "warning", "content": "Previous hash mismatch"}

        # Validate transactions in data field
        if content["data"]:
            if not isinstance(content["data"], list):
                warning_msg = f"⚠️ [Dev Warning] Block data must be a list. Received: {type(content['data'])}. Data: {content['data']}"
                print(warning_msg)
                logger.warning(warning_msg)
                return {"type": "warning", "content": "Block data must be a list of transactions"}

            for txn in content["data"]:
                required_txn_fields = {"sender", "recipient", "amount"}
                if not required_txn_fields.issubset(txn):
                    missing_fields = required_txn_fields - txn.keys()
                    warning_msg = (
                        f"⚠️ [Dev Warning] Transaction missing fields. 🧩 Missing: {missing_fields}. Transaction: {txn}"
                    )
                    print(warning_msg)
                    logger.warning(warning_msg)
                    return {"type": "warning", "content": "Transaction format invalid"}

        # Insert block into the database
        logger.debug(f"📥 Inserting block into database: {content}")
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
        print(f"✅ [Dev Info] Block successfully added. 🏷️ Hash: {content['hash']}")
        logger.info(f"✅ Block successfully added. 🏷️ Hash: {content['hash']}")

    except Exception as e:
        error_msg = f"🚨 [Dev Warning] Error processing block. 🔧 Details: {e}. Block: {content}"
        print(error_msg)
        logger.error(error_msg)
        return {"type": "error", "content": "Failed to process block"}

    finally:
        conn.close()
        logger.debug("🔒 Database connection closed.")
        print("🔒 [Dev Info] Database connection closed.")

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


async def handle_new_peer(content):
    """Process the new peer message."""
    peer_url = content.get("peer_url")
    if not peer_url:
        logger.error("Received invalid new_peer message without peer_url.")
        return

    if peer_url not in PEERS:
        add_peer_to_db(peer_url)
        add_peer(peer_url)
        logger.info(f"New peer added dynamically: {peer_url}")

async def broadcast_new_peer(peer_url):
    """Broadcast the new peer to all connected peers."""
    message = {
        "type": "new_peer",
        "content": {"peer_url": peer_url}
    }
    await broadcast_message_to_peers(message)
    logger.info(f"Broadcasted new peer to the network: {peer_url}")

