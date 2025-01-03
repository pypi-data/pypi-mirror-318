import json
from pathlib import Path
import requests
from sallmon.sallmon_core.services.db import save_message  # Import save_message function

# Define the path for the peers file
PEERS_FILE = Path("~/.sallmon/peers.json").expanduser()

# Load peers from file
def load_peers():
    if PEERS_FILE.exists():
        with open(PEERS_FILE, "r") as file:
            return set(json.load(file))  # Load as a set for uniqueness
    return set()

# Save peers to file
def save_peers(peers):
    with open(PEERS_FILE, "w") as file:
        json.dump(list(peers), file)  # Save as a list to make it JSON serializable

# Initialize peers
peers = load_peers()

def add_peer(peer_ip: str):
    if peer_ip not in peers:
        peers.add(peer_ip)
        save_peers(peers)
        return True  # Peer added
    return False  # Peer already exists

def remove_peer(peer_ip: str):
    if peer_ip in peers:
        peers.discard(peer_ip)
        save_peers(peers)

def get_peers():
    return list(peers)

def broadcast_message(message: dict):
    """Broadcast a message to all peers and store it in the database."""
    responses = []
    for peer in peers:
        try:
            url = f"http://{peer}/send-to-ws"
            response = requests.post(url, json=message)
            responses.append({"peer": peer, "response": response.json()})
        except Exception as e:
            responses.append({"peer": peer, "error": str(e)})

    # Store the message in the database only if it was successfully broadcasted
    save_message(message)
    return responses

