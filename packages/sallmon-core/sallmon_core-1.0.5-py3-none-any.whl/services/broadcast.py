import json
import logging

logger = logging.getLogger("broadcast")

# Peer Connections
peer_connections = {}

async def broadcast_to_peers(data):
    """Broadcast a message to all connected peers."""
    logger.info(f"🌍 Broadcasting to peers: {json.dumps(data, indent=2)}")
    peers_to_remove = []

    for peer_url, websocket in list(peer_connections.items()):
        try:
            logger.info(f"🔗 Sending to peer: {peer_url}")
            await websocket.send(json.dumps(data))
            logger.info(f"✅ Successfully sent to peer: {peer_url}")
        except Exception as e:
            logger.error(f"❌ Failed to send message to peer {peer_url}: {e}")
            peers_to_remove.append(peer_url)

    for peer_url in peers_to_remove:
        logger.warning(f"⚠️ Removing failed peer connection: {peer_url}")
        del peer_connections[peer_url]

async def broadcast_to_clients(data, exclude=None):
    """Broadcast a message to all connected WebSocket clients."""
    logger.info(f"🖥️ Broadcasting to WebSocket clients: {json.dumps(data, indent=2)}")
    for client in connected_clients:
        if client != exclude:
            try:
                logger.info(f"📤 Sending to client: {client}")
                await client.send_text(json.dumps(data))
                logger.info(f"✅ Successfully sent to client: {client}")
            except Exception as e:
                logger.error(f"❌ Error sending to client: {client} - {e}")
                connected_clients.remove(client)
