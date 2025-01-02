import logging
from datetime import datetime
from fastapi import APIRouter, HTTPException, Request
from ..services.peers import broadcast_message_to_peers

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


@api_router.get("/get-mempool/")
async def get_mempool():
    """Retrieve the current mempool transactions."""
    try:
        conn = sqlite3.connect(os.path.expanduser("~/.sallmon/blockchain.db"))
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()
        conn.close()

        return {"status": "success", "mempool": transactions}
    except Exception as e:
        logger.error(f"Failed to retrieve mempool: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving mempool")
