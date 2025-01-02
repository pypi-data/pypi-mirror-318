import sqlite3
import logging
from datetime import datetime
from fastapi import APIRouter, HTTPException, Request
from ..services.peers import broadcast_message_to_peers, PEERS
import requests
from typing import List
import os

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
        cursor.execute("SELECT * FROM blocks ORDER BY block_index ASC")
        blocks = cursor.fetchall()
        conn.close()

        # Format blocks into a list of dictionaries
        formatted_blocks = [
            {
                "block_index": block[0],
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


@api_router.post("/broadcast-transaction/")
async def broadcast_transaction(request: Request, transaction: dict):
    """Broadcast a transaction to all peers."""
    log_request(request, "/broadcast-transaction/")
    try:
        logger.info(f"Broadcasting transaction: {transaction}")
        validate_fields(transaction, ["sender", "recipient", "amount"])  # Add validation
        await broadcast_message_to_peers({
            "type": "transaction",
            "content": transaction
        })
        logger.info(f"✅ Transaction broadcasted successfully. Details: {transaction}")
        return {"status": "success", "message": "Transaction broadcasted to all peers"}
    except ValueError as e:
        logger.warning(f"Validation Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@api_router.post("/broadcast-block/")
async def broadcast_block(request: Request, block: dict):
    """Broadcast a block to all peers."""
    log_request(request, "/broadcast-block/")
    try:
        logger.info(f"Broadcasting block: {block}")
        validate_fields(block, ["index", "previous_hash", "timestamp", "hash", "data"])  # Add validation
        await broadcast_message_to_peers({
            "type": "block",
            "content": block
        })
        logger.info(f"✅ Block broadcasted successfully. Details: {block}")
        return {"status": "success", "message": "Block broadcasted to all peers"}
    except ValueError as e:
        logger.warning(f"Validation Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")


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

logger = logging.getLogger("blockchain_sync")
logging.basicConfig(level=logging.INFO)

# Hardcoded peer list
PEERS = ["http://96.70.45.233:1337/blocks/", "http://172.234.207.57:1337/blocks/"]

# Hardcoded peer list
PEERS = ["http://96.70.45.233:1337/blocks/", "http://172.234.207.57:1337/blocks/"]

@api_router.get("/blocks")
async def sync_with_peers():
    """
    Fetch and synchronize with the longest blockchain from hardcoded peers.
    """
    try:
        longest_chain = []
        
        for peer_url in PEERS:
            try:
                logger.info(f"Fetching blocks from {peer_url}")
                
                # Make a GET request to the peer's /blocks/ endpoint
                response = requests.get(peer_url, timeout=5)
                response.raise_for_status()  # Raise an error for non-2xx status codes
                
                peer_blocks = response.json().get("blocks", [])
                logger.info(f"Received {len(peer_blocks)} blocks from {peer_url}")

                # Check if this peer has the longest chain
                if len(peer_blocks) > len(longest_chain):
                    longest_chain = peer_blocks
            except requests.RequestException as e:
                logger.error(f"Failed to fetch blocks from {peer_url}: {e}")

        if not longest_chain:
            raise HTTPException(status_code=404, detail="No valid blockchains found from peers.")

        logger.info(f"Longest blockchain has {len(longest_chain)} blocks.")
        return {
            "status": "success",
            "longest_blockchain": longest_chain,
        }
    except HTTPException as e:
        logger.warning(f"HTTP Exception occurred: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error syncing with peers: {e}")
        raise HTTPException(status_code=500, detail="Failed to sync blockchain with peers.")


@api_router.post("/announce-peer/")
async def announce_peer(request: Request, peer: dict):
    """Handle peer announcements."""
    peer_url = peer.get("peer_url")
    if not peer_url:
        raise HTTPException(status_code=400, detail="Peer URL is required.")

    logger.info(f"Received peer announcement: {peer_url}")
    add_peer_to_db(peer_url)

    # Optionally broadcast this peer to others
    await broadcast_new_peer(peer_url)
    return {"status": "success", "message": f"Peer {peer_url} announced successfully."}
