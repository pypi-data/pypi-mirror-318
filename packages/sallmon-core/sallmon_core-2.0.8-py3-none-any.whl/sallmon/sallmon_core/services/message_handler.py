import hashlib
from sallmon.sallmon_core.services.db import save_message
from sallmon.sallmon_core.services.peers import broadcast_message
from datetime import datetime, timezone
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] 🛠 %(message)s")


def generate_message_id(content):
    """Generate a unique ID for a message."""
    return hashlib.sha256(json.dumps(content, sort_keys=True).encode()).hexdigest()



# Updated message handler for "mempool"
from sallmon.sallmon_core.services.mempool import mempool
from sallmon.sallmon_core.services.utxos import validate_transaction  # Placeholder for transaction validation

async def process_message(message: dict):
    """
    Process incoming messages with a simplified set of types: 'ping', 'mempool', 'blocks'.
    """
    logging.info("📩 Received message: %s", message)

    # Extract and validate message type
    message_type = message.get("type")
    if not message_type:
        logging.error("🚨 Message type is missing!")
        return {"status": "error", "message": "Message type is required"}

    # Handle "ping"
    if message_type == "ping":
        logging.info("🏓 Ping received, responding with Pong.")
        return {"status": "success", "message": "pong"}

    # Handle "mempool"

    # Handle "mempool"
    elif message_type == "mempool":
        logging.info("🗂️ Processing message for mempool...")

        # Extract transaction details
        transaction_id = message.get("transaction_id")
        transaction = message.get("transaction")

        if not transaction_id or not transaction:
            logging.error("🚨 Invalid message: Missing transaction_id or transaction data.")
            return {"status": "error", "message": "Invalid message format."}

        # Validate the transaction
        is_valid, validation_message = validate_transaction(transaction)
        if not is_valid:
            logging.warning(f"🚨 Invalid transaction: {validation_message}")
            return {"status": "error", "message": f"Invalid transaction: {validation_message}"}

        # Add the transaction to the mempool
        success = mempool.add_transaction(transaction_id, transaction)
        if success:
            logging.info("✅ Transaction added to mempool successfully.")
            return {"status": "success", "message": "Transaction added to mempool."}
        else:
            logging.warning("🚨 Duplicate transaction detected.")
            return {"status": "error", "message": "Duplicate transaction."}

    # Handle "blocks"
    #elif message_type == "blocks":
        #logging.info("📦 Processing block message...")
        # Placeholder logic for blocks
        #save_message(message)
        #return {"status": "success", "message": "Block message processed"}

    # Handle "blocks"
    elif message_type == "blocks":
        logging.info("📦 Processing block message...")

        # Extract block data from the message
        block_data = message.get("block_data")
        if not block_data:
            logging.error("🚨 Missing 'block_data' in the message.")
            return {"status": "error", "message": "Missing 'block_data' in message."}

         # Send block data to the /blocks endpoint
        try:
            response = requests.post("http://127.0.0.1:1337/blocks", json=block_data)
            if response.status_code == 200:
                logging.info("✅ Block added successfully through the endpoint.")
                return {"status": "success", "message": "Block added successfully through the endpoint."}
            else:
                logging.warning(f"🚨 Failed to add block: {response.json()}")
                return {"status": "error", "message": f"Failed to add block: {response.json()}"}
        except Exception as e:
            logging.error(f"🚨 Error while sending block to the endpoint: {e}")
            return {"status": "error", "message": "Error while sending block to the endpoint."}


    # Handle "join-network"
    elif message_type == "join-network":
        peer_ip = message.get("content", {}).get("ip")
        if not peer_ip:
            logging.error("🚨 Join-network message missing peer IP!")
            return {"status": "error", "message": "Peer IP is required"}

        # Add the peer and broadcast if successfully addedc
        from sallmon.sallmon_core.services.peers import add_peer
        if add_peer(peer_ip):
            logging.info(f"🌐 New peer added: {peer_ip}")
            return {"status": "success", "message": f"Peer {peer_ip} added to the network"}
        else:
            logging.info(f"🌐 Peer {peer_ip} already exists.")
            return {"status": "success", "message": f"Peer {peer_ip} already exists"}

    # Default: Unknown type
    else:
        logging.warning("❓ Unknown message type: %s", message_type)
        return {"status": "error", "message": f"Unknown message type: {message_type}"}
