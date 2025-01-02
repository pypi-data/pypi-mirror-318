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
async def fetch_local_blocks():
    """Fetch blocks from the local server."""
    try:
        # Path to the local blockchain database
        db_path = os.path.expanduser("~/.sallmon/blockchain.db")
        if not os.path.exists(db_path):
            logger.error(f"Blockchain database not found at {db_path}")
            raise HTTPException(status_code=404, detail="Blockchain database not found.")

        # Connect to the database and fetch blocks
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM blocks ORDER BY index ASC")
        blocks = cursor.fetchall()
        conn.close()

        # Format blocks into a list of dictionaries
        formatted_blocks = [
            {
                "index": block[0],
                "previous_hash": block[1],
                "timestamp": block[2],
                "data": block[3],
                "hash": block[4],
            }
            for block in blocks
        ]

        if not formatted_blocks:
            raise HTTPException(status_code=404, detail="No blocks found.")

        return {
            "status": "success",
            "blocks": formatted_blocks,
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Unexpected error fetching local blocks: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch blocks.")


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

@api_router.get("/blocks")
async def sync_with_peers():
    """Fetch and synchronize with the longest blockchain from peers."""
    try:
        logger.info("Fetching blockchains from peers...")
        longest_chain = []
        for peer in PEERS:
            try:
                # Construct peer's /blocks/ endpoint
                peer_url = peer.replace("ws", "http").replace("/ws", "/blocks/")
                logger.info(f"Fetching blocks from {peer_url}")
                response = requests.get(peer_url, timeout=5)
                response.raise_for_status()

                peer_blocks = response.json().get("blocks", [])
                logger.info(f"Received {len(peer_blocks)} blocks from {peer_url}")

                # Check if this chain is the longest
                if len(peer_blocks) > len(longest_chain):
                    longest_chain = peer_blocks
            except Exception as e:
                logger.error(f"Failed to fetch blocks from {peer}: {e}")

        if not longest_chain:
            raise HTTPException(status_code=404, detail="No valid blockchains found from peers.")

        logger.info(f"Longest blockchain has {len(longest_chain)} blocks.")
        return {
            "status": "success",
            "longest_blockchain": longest_chain,
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Unexpected error syncing with peers: {e}")
        raise HTTPException(status_code=500, detail="Failed to sync blockchain with peers.")
