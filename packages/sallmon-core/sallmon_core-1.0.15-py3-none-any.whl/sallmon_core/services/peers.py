import json
import logging
import asyncio
import websockets

logger = logging.getLogger("peers")

# Hardcoded peers
PEERS = [
    "ws://96.70.45.233:1337/ws",
    "ws://172.234.207.57:1337/ws"
]

async def send_message_to_peer(peer_url: str, message: dict):
    """Send a message to a peer and wait for a response."""
    logger.info(f"Connecting to peer: {peer_url}")
    try:
        async with websockets.connect(peer_url) as websocket:
            logger.info(f"Connected to peer: {peer_url}")
            await websocket.send(json.dumps(message))
            logger.info(f"Message sent to {peer_url}: {message}")
            response = await websocket.recv()
            logger.info(f"Response received from {peer_url}: {response}")
            return response
    except Exception as e:
        logger.error(f"Failed to send message to {peer_url}: {e}")
        return None

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
