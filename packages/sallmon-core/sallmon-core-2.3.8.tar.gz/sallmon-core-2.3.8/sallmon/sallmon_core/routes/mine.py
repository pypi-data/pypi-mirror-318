from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sallmon.sallmon_core.services.mining import mine_block
import logging

router = APIRouter()

class MineBlockRequest(BaseModel):
    miner_address: str
    resource_cost: float

@router.post("/mine-block")
def api_mine_block(request: MineBlockRequest):
    """API endpoint to mine a new block."""
    try:
        logging.info(f"Mining request received: {request}")
        block = mine_block(request.miner_address, request.resource_cost)
        if block:
            logging.info(f"Block mined successfully: {block}")
            return {"status": "success", "block": block["block"], "fmv": block["fmv"], "msrp": block["msrp"], "rewards": block["rewards"]}
        else:
            logging.error("Failed to mine block.")
            raise HTTPException(status_code=500, detail="Failed to mine block.")
    except Exception as e:
        logging.error(f"Error in mining endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))
