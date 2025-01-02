import logging
from datetime import datetime
from fastapi import APIRouter, HTTPException, Request
from ..services.peers import broadcast_message_to_peers, PEERS
import requests
from typing import List

api_router = APIRouter()
logger = logging.getLogger("api")

def log_request(request: Request, endpoint: str):
    """Log incoming request details."""
    logger.info(f"📩 [REQUEST] Endpoint: {endpoint}, Time: {datetime.now()}")
    logger.debug(f"Headers: {request.headers}")
    logger.debug(f"Client IP: {request.client.host}")

def validate_fields(data: dict, required_fields: list):
    """Ensure all required fields are present in the data."""
    missing = [field for field in required_fields if field not in data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

@api_router.get("/blocks/")
async def fetch_peer_blocks():
    """Fetch and aggregate blocks from all peers."""
    try:
        logger.info("Fetching blocks from peers...")
        blocks = []
        for peer in PEERS:
            try:
                # Assuming peers have an HTTP API at /blocks
                peer_url = peer.replace("ws", "http").replace("/ws", "/blocks")
                logger.info(f"Fetching blocks from {peer_url}")
                response = requests.get(peer_url, timeout=5)
                response.raise_for_status()
                peer_blocks = response.json().get("blocks", [])
                blocks.extend(peer_blocks)
            except Exception as e:
                logger.error(f"Failed to fetch blocks from {peer}: {e}")
        
        if not blocks:
            raise HTTPException(status_code=404, detail="No blocks found from peers.")
        
        return {
            "status": "success",
            "blocks": blocks,
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Unexpected error fetching blocks from peers: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch blocks from peers")

@api_router.post("/broadcast-message/")
async def broadcast_message(request: Request, message: dict):
    """Broadcast a message to all peers."""
    log_request(request, "/broadcast-message/")
    try:
        logger.info(f"Broadcast request received: {message}")
        validate_fields(message, ["type", "content"])  # Add validation
        await broadcast_message_to_peers(message)
        logger.info("✅ Message broadcasted successfully.")
        return {"status": "success", "message": "Message broadcasted to all peers"}
    except ValueError as e:
        logger.warning(f"Validation Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to broadcast message")

@api_router.get("/get-mempool/")
async def get_mempool():
    """Retrieve the current mempool transactions."""
    try:
        # Logic for retrieving mempool transactions
        pass
    except Exception as e:
        logger.error(f"Failed to retrieve mempool: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving mempool")
