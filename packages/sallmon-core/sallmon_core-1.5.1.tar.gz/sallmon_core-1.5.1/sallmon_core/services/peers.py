
import sqlite3
import os
import json
import logging
import asyncio
import websockets
from pathlib import Path
from typing import Dict, Any
import requests

logger = logging.getLogger("peers")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")


# Hardcoded peers
HARD_CODED_PEERS = [
    "ws://96.70.45.233:1337/ws",
    "ws://172.234.207.57:1337/ws",
    "ws://172.234.203.211:1337/ws",
]

# Global peers list initialized with hardcoded peers
PEERS = HARD_CODED_PEERS[:]

# Print the list of hardcoded peers
print("Hardcoded Peers:", HARD_CODED_PEERS)

# Print the list of hardcoded peers
print("Hardcoded Peers:", HARD_CODED_PEERS)

# Print the list of hardcoded peers
print("Hardcoded Peers:", HARD_CODED_PEERS)


# Initialize the peers list
PEERS = HARD_CODED_PEERS[:]
PEER_STATUSES = {}  # Store the status of each peer

# File to store dynamically added peers
PEERS_FILE = Path("dynamic_peers.json")

# Initialize the peers list with hardcoded peers
PEERS = HARD_CODED_PEERS[:]
PEER_STATUSES: Dict[str, str] = {}  # Store the status of each peer

def get_db_connection():
    """Get a database connection."""
    db_path = os.path.expanduser("~/.sallmon/blockchain.db")
    conn = sqlite3.connect(db_path)
    return conn

def load_dynamic_peers():
    """Load peers from the database and dynamic peers file."""
    global PEERS
    logger.info("Loading peers from the database and file...")

    # Load peers from the database
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS peers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                peer_url TEXT UNIQUE NOT NULL
            )
        ''')
        db_conn.commit()

        cursor.execute("SELECT peer_url FROM peers")
        db_peers = [row[0] for row in cursor.fetchall()]
        logger.info(f"📂 Loaded {len(db_peers)} peers from the database.")

        for peer in db_peers:
            if peer not in PEERS:
                PEERS.append(peer)
    except Exception as e:
        logger.error(f"❌ Failed to load peers from the database: {e}")
    finally:
        db_conn.close()

    # Load dynamic peers from the file
    if PEERS_FILE.exists():
        try:
            with PEERS_FILE.open("r") as f:
                dynamic_peers = json.load(f)
                for peer in dynamic_peers:
                    if peer not in PEERS:
                        PEERS.append(peer)
            logger.info(f"📂 Loaded peers from file: {dynamic_peers}")
        except Exception as e:
            logger.error(f"❌ Failed to load peers from file: {e}")
    else:
        logger.info("No dynamic peers file found.")

    logger.info(f"✅ Total peers loaded: {len(PEERS)}")


# Load peers from the database, dynamic peers file, and hardcoded list
def load_peers_from_db():
    """Load peers from the database and ensure they are in the PEERS list."""
    global PEERS
    db_conn = get_db_connection()
    cursor = db_conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS peers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                peer_url TEXT UNIQUE NOT NULL
            )
        ''')
        db_conn.commit()

        cursor.execute("SELECT peer_url FROM peers")
        db_peers = [row[0] for row in cursor.fetchall()]
        logger.info(f"📂 Loaded {len(db_peers)} peers from the database.")

        for peer in db_peers:
            if peer not in PEERS:
                PEERS.append(peer)

        # Load dynamic peers
        if PEERS_FILE.exists():
            with PEERS_FILE.open("r") as f:
                dynamic_peers = json.load(f)
                for peer in dynamic_peers:
                    if peer not in PEERS:
                        PEERS.append(peer)

        logger.info(f"✅ Total peers loaded: {len(PEERS)}")
    except Exception as e:
        logger.error(f"❌ Failed to load peers: {e}")
    finally:
        db_conn.close()

# Save dynamic peers to the file
def save_dynamic_peers():
    """Save non-hardcoded peers to the dynamic peers file."""
    try:
        dynamic_peers = [peer for peer in PEERS if peer not in HARD_CODED_PEERS]
        with PEERS_FILE.open("w") as f:
            json.dump(dynamic_peers, f)
        logger.info(f"✅ Saved {len(dynamic_peers)} dynamic peers to file.")
    except Exception as e:
        logger.error(f"❌ Failed to save dynamic peers: {e}")

def add_peer(peer_url: str):
    """Add a new peer to the list and save it."""
    if peer_url not in PEERS:
        PEERS.append(peer_url)
        PEER_STATUSES[peer_url] = "unknown"  # Initialize status
        save_dynamic_peers()
        add_peer_to_db(peer_url)  # Ensure it's added to the database
        logger.info(f"✅ Added new peer: {peer_url}")
    else:
        logger.info(f"Peer already exists: {peer_url}")

def add_peer_to_db(peer_url):
    """Add a peer to the database, ensuring no duplicates."""
    db_conn = get_db_connection()
    cursor = db_conn.cursor()

    try:
        cursor.execute('''
            INSERT OR IGNORE INTO peers (peer_url)
            VALUES (?)
        ''', (peer_url,))
        db_conn.commit()
        logger.info(f"✅ Peer {peer_url} added to the database.")
    except Exception as e:
        logger.error(f"❌ Failed to add peer {peer_url} to the database: {e}")
    finally:
        db_conn.close()

# Other existing methods remain unchanged

# Validate a peer
async def validate_peer(peer_url: str) -> bool:
    """Check if a peer is reachable and responsive."""
    logger.info(f"Validating peer: {peer_url}")
    try:
        async with websockets.connect(peer_url, timeout=5) as websocket:
            await websocket.send(json.dumps({"type": "heartbeat", "content": {}}))
            response = await websocket.recv()
            response_data = json.loads(response)
            if response_data.get("type") == "heartbeat_ack":
                logger.info(f"Peer {peer_url} is valid and responsive.")
                PEER_STATUSES[peer_url] = "online"
                return True
    except Exception as e:
        logger.warning(f"Validation failed for peer {peer_url}: {e}")
    PEER_STATUSES[peer_url] = "offline"
    return False

# Remove unreachable peers
def remove_peer(peer_url: str):
    """Remove a peer from the list and update the file."""
    if peer_url in HARD_CODED_PEERS:
        logger.warning(f"Attempted to remove hardcoded peer: {peer_url}. Operation ignored.")
        return  # Do nothing for hardcoded peers

    if peer_url in PEERS:
        PEERS.remove(peer_url)
        PEER_STATUSES.pop(peer_url, None)
        save_dynamic_peers()
        logger.info(f"Removed unreachable peer: {peer_url}")

# Send a message to a single peer
async def send_message_to_peer(peer_url: str, message: Dict[str, Any]):
    """Send a message to a peer and wait for a response."""
    logger.info(f"Connecting to peer: {peer_url}")
    try:
        async with websockets.connect(peer_url, timeout=5) as websocket:
            logger.info(f"Connected to peer: {peer_url}")
            await websocket.send(json.dumps(message))
            logger.info(f"Message sent to {peer_url}: {message}")
            response = await websocket.recv()
            logger.info(f"Response received from {peer_url}: {response}")
            return json.loads(response)
    except Exception as e:
        logger.error(f"Failed to send message to {peer_url}: {e}")
        remove_peer(peer_url)  # Remove peer if communication fails
        return None

# Broadcast a message to all peers
async def broadcast_message_to_peers(message: Dict[str, Any]):
    """Broadcast a message to all peers and log responses."""
    global PEERS

    # Fetch current list of peers from the database
    def fetch_peers_from_db():
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT peer_url FROM peers")
            db_peers = [row[0] for row in cursor.fetchall()]
            conn.close()

            logger.info(f"🔍 Fetched peers from database: {db_peers}")
            return db_peers
        except Exception as e:
            logger.error(f"❌ Failed to fetch peers from database: {e}")
            return []

    # Fetch and update the global PEERS list
    db_peers = fetch_peers_from_db()
    PEERS = list(set(HARD_CODED_PEERS + db_peers))  # Merge hardcoded peers with database peers
    logger.info(f"🌐 Current list of peers for broadcasting: {PEERS}")

    # Start broadcasting
    logger.info(f"📣 Broadcasting message to all peers: {message}")
    tasks = [send_message_to_peer(peer, message) for peer in PEERS]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Log detailed responses
    for peer, result in zip(PEERS, results):
        if isinstance(result, Exception):
            logger.error(f"❌ Error broadcasting to {peer}: {result}")
        else:
            logger.info(f"✅ Successful response from {peer}: {result}")

    logger.info(f"🛑 Broadcast completed for all peers.")

# Handle chat messages
async def handle_chat_message(sender: str, message: str):
    """Handle and broadcast a chat message to all peers."""
    chat_message = {
        "type": "chat",
        "content": {"sender": sender, "message": message}
    }
    logger.info(f"Broadcasting chat message: {chat_message}")
    await broadcast_message_to_peers(chat_message)

# Handle admin commands
async def handle_command(action: str, params: Dict[str, Any]):
    """Process and broadcast an admin command."""
    command_message = {
        "type": "command",
        "content": {"action": action, "params": params}
    }
    logger.info(f"Broadcasting command: {command_message}")
    await broadcast_message_to_peers(command_message)


import threading

# Lock for thread safety
blockchain_sync_lock = threading.Lock()


def sync_blockchain():
    """
    Sync the local blockchain with the longest chain found among peers.
    Always replaces the local blockchain with the longest one found.
    """
    logger.info("Starting blockchain synchronization...")
    longest_chain = fetch_longest_blockchain()

    if longest_chain:
        logger.info(f"Longest blockchain found with {len(longest_chain)} blocks.")
        
        # Directly replace the local blockchain with the longest chain
        try:
            save_local_blockchain(longest_chain)
            logger.info("Blockchain synchronized successfully.")
        except Exception as e:
            logger.error(f"Failed to save blockchain: {e}")
    else:
        logger.warning("No valid blockchain found from peers. Sync skipped.")


def fetch_longest_blockchain():
    """Fetch the longest blockchain from all peers."""
    longest_chain = []
    for peer in PEERS:
        http_url = f"{peer.replace('ws://', 'http://').replace('/ws', '/blocks/')}"
        try:
            logger.info(f"Attempting to fetch blockchain from: {http_url}")
            response = requests.get(http_url, timeout=5)
            response.raise_for_status()
            peer_chain = response.json().get("blocks", [])
            
            # Validate blocks
            for block in peer_chain:
                if "index" not in block:
                    logger.warning(f"Block missing 'index': {block}")
                    continue

            if len(peer_chain) > len(longest_chain):
                longest_chain = peer_chain
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch blockchain from {http_url}: {e}")
    return longest_chain



def validate_blockchain(blockchain):
    """Validate the structure and integrity of the blockchain."""
    if not blockchain:
        return False

    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]

        # Check the hash of the previous block
        if current_block["previous_hash"] != previous_block["hash"]:
            logger.error(f"Blockchain validation failed at block {i}.")
            return False

    logger.info("Blockchain validation successful.")
    return True

import sqlite3

from pathlib import Path
def save_local_blockchain(blockchain):
    db_path = Path("~/.sallmon/blockchain.db").expanduser()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)

    try:
        cursor = conn.cursor()

        # Ensure the blocks table exists
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
        conn.commit()

        # Fetch local block indices
        cursor.execute('SELECT block_index FROM blocks')
        local_blocks = {row[0] for row in cursor.fetchall()}
        logger.info(f"🗄️ Local blocks found: {local_blocks}")

        # Save all missing blocks
        for block in blockchain:
            if block["block_index"] not in local_blocks:
                if validate_block(block):
                    logger.info(f"✅ Valid block {block['block_index']} passed validation.")
                else:
                    logger.warning(f"⚠️ Invalid block {block['block_index']} detected but will be saved (dev mode).")
                
                # Save block regardless of validation
                cursor.execute('''
                    INSERT INTO blocks (block_index, previous_hash, timestamp, data, hash)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    block["block_index"],
                    block["previous_hash"],
                    block["timestamp"],
                    json.dumps(block["data"]),
                    block["hash"]
                ))
                logger.info(f"📥 Block {block['block_index']} saved to database.")
        conn.commit()
    except sqlite3.Error as sql_e:
        logger.error(f"🚨 SQLite error occurred: {sql_e}")
        raise
    except Exception as e:
        logger.error(f"❌ Failed to save blockchain: {e}")
        raise
    finally:
        conn.close()
        logger.debug("🔒 Database connection closed.")

async def broadcast_new_peer(peer_url):
    message = {
        "type": "new_peer",
        "content": {"peer_url": peer_url}
    }
    await broadcast_message_to_peers(message)
    logger.info(f"Broadcasted new peer: {peer_url}")

# Periodically validate peers
async def periodic_peer_validation(interval: int = 60):
    """Periodically validate peers to ensure the list is up-to-date."""
    while True:
        logger.info("Starting periodic peer validation...")
        for peer in PEERS[:]:
            if not await validate_peer(peer):
                logger.warning(f"Peer {peer} is unreachable and will be removed.")
                remove_peer(peer)
        logger.info("Peer validation complete.")
        await asyncio.sleep(interval)

# Load dynamic peers at startup
load_dynamic_peers()

# Inside services/peers.py

# Validate a peer
async def validate_peer(peer_url: str) -> bool:
    """Validate that the peer is reachable."""
    logger.info(f"Validating peer: {peer_url}")
    try:
        async with websockets.connect(peer_url) as websocket:
            await websocket.send(json.dumps({"type": "heartbeat", "content": {}}))
            response = await websocket.recv()
            response_data = json.loads(response)
            if response_data.get("type") == "heartbeat_ack":
                logger.info(f"Peer {peer_url} is valid and responsive.")
                return True
    except Exception as e:
        logger.warning(f"Failed to validate peer {peer_url}: {e}")
        return False

def validate_block(block):
    required_fields = ["block_index", "previous_hash", "timestamp", "data", "hash"]
    for field in required_fields:
        if field not in block or block[field] in [None, {}, ""]:
            logger.warning(f"Block is invalid: Missing or empty field {field}")
            return False

    # Validate block index
    if not isinstance(block["block_index"], int):
        logger.warning(f"Invalid block index: {block['block_index']}")
        return False

    # Validate transactions (skip for genesis block)
    if block["block_index"] > 0 and (not isinstance(block["data"], list) or not block["data"]):
        logger.warning(f"Block has invalid transactions: {block['data']}")
        return False

    return True
