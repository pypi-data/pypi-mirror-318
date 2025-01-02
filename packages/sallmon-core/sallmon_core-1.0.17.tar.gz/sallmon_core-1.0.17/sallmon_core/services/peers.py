import json
import logging
import asyncio
import websockets
from pathlib import Path

logger = logging.getLogger("peers")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Hardcoded peers
HARD_CODED_PEERS = [
    "ws://96.70.45.233:1337/ws",
    "ws://172.234.207.57:1337/ws"
]

# File to store dynamically added peers
PEERS_FILE = Path("dynamic_peers.json")

# Initialize the peers list with hardcoded peers
PEERS = HARD_CODED_PEERS[:]
PEER_STATUSES = {}  # Store the status of each peer

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
            await websocket.send(json.dumps({"type": "ping"}))
            response = await websocket.recv()
            if response == "pong":
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
    if peer_url in PEERS:
        PEERS.remove(peer_url)
        PEER_STATUSES.pop(peer_url, None)
        save_dynamic_peers()
        logger.info(f"Removed unreachable peer: {peer_url}")

# Send a message to a single peer
async def send_message_to_peer(peer_url: str, message: dict):
    """Send a message to a peer and wait for a response."""
    logger.info(f"Connecting to peer: {peer_url}")
    try:
        async with websockets.connect(peer_url, timeout=5) as websocket:
            logger.info(f"Connected to peer: {peer_url}")
            await websocket.send(json.dumps(message))
            logger.info(f"Message sent to {peer_url}: {message}")
            response = await websocket.recv()
            logger.info(f"Response received from {peer_url}: {response}")
            return response
    except Exception as e:
        logger.error(f"Failed to send message to {peer_url}: {e}")
        remove_peer(peer_url)  # Remove peer if communication fails
        return None

# Broadcast a message to all peers
async def broadcast_message_to_peers(message: dict):
    """Broadcast a message to all peers and log responses."""
    logger.info(f"Broadcasting message to all peers: {message}")
    tasks = [send_message_to_peer(peer, message) for peer in PEERS]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for peer, result in zip(PEERS, results):
        if isinstance(result, Exception):
            logger.error(f"Error with {peer}: {result}")
        else:
            logger.info(f"Response from {peer}: {result}")

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
