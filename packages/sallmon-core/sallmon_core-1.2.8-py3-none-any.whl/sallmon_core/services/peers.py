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
    "ws://172.234.207.57:1337/ws"
]

# File to store dynamically added peers
PEERS_FILE = Path("dynamic_peers.json")

# Initialize the peers list with hardcoded peers
PEERS = HARD_CODED_PEERS[:]
PEER_STATUSES: Dict[str, str] = {}  # Store the status of each peer

# Load dynamic peers from the file
def load_dynamic_peers():
    """Load dynamic peers from a file and add them to the PEERS list."""
    if PEERS_FILE.exists():
        try:
            with PEERS_FILE.open("r") as f:
                dynamic_peers = json.load(f)
                logger.info(f"Loaded {len(dynamic_peers)} dynamic peers from file.")
                for peer in dynamic_peers:
                    if peer not in PEERS:
                        PEERS.append(peer)
        except Exception as e:
            logger.error(f"Failed to load dynamic peers: {e}")
    else:
        logger.info("No dynamic peers file found.")

# Save dynamic peers to the file
def save_dynamic_peers():
    """Save non-hardcoded peers to the dynamic peers file."""
    try:
        dynamic_peers = [peer for peer in PEERS if peer not in HARD_CODED_PEERS]
        with PEERS_FILE.open("w") as f:
            json.dump(dynamic_peers, f)
        logger.info(f"Saved {len(dynamic_peers)} dynamic peers to file.")
    except Exception as e:
        logger.error(f"Failed to save dynamic peers: {e}")

# Add a new peer to the list
def add_peer(peer_url: str):
    """Add a new peer to the list and save it."""
    if peer_url not in PEERS:
        PEERS.append(peer_url)
        PEER_STATUSES[peer_url] = "unknown"  # Initialize status
        save_dynamic_peers()
        logger.info(f"Added new peer: {peer_url}")
    else:
        logger.info(f"Peer already exists: {peer_url}")

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
    logger.info(f"Broadcasting message to all peers: {message}")
    tasks = [send_message_to_peer(peer, message) for peer in PEERS]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for peer, result in zip(PEERS, results):
        if isinstance(result, Exception):
            logger.error(f"Error with {peer}: {result}")
        else:
            logger.info(f"Response from {peer}: {result}")

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
            if len(peer_chain) > len(longest_chain):
                longest_chain = peer_chain
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch blockchain from {http_url}: {e}")
            logger.error(f"To debug, use: curl -X GET {http_url}")
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

def save_local_blockchain(blockchain):
    """
    Save the blockchain locally into an SQLite database.
    """
    db_path = "blockchain.db"  # Path to the SQLite database
    conn = sqlite3.connect(db_path)

    try:
        cursor = conn.cursor()

        # Ensure the blocks table exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS blocks (
                block_index INTEGER PRIMARY KEY,
                previous_hash TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                data TEXT NOT NULL,
                hash TEXT NOT NULL
            )
        ''')
        conn.commit()

        # Clear existing blocks
        cursor.execute('DELETE FROM blocks')
        conn.commit()

        # Insert new blockchain
        for block in blockchain:
            cursor.execute('''
                INSERT INTO blocks (index, previous_hash, timestamp, data, hash)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                block['index'],
                block['previous_hash'],
                block['timestamp'],
                json.dumps(block['data']),  # Serialize data to JSON
                block['hash']
            ))
        conn.commit()

        logger.info(f"Blockchain saved to database with {len(blockchain)} blocks.")
    except Exception as e:
        logger.error(f"Failed to save blockchain to database: {e}")
        raise
    finally:
        conn.close()


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
