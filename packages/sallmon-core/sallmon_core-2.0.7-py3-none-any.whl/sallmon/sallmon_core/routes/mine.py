from fastapi import APIRouter, HTTPException
from sallmon_core.services.mining import mine_block

router = APIRouter()

@router.post("/mine-block")
def api_mine_block(miner_address: str):
    """API endpoint to mine a new block."""
    try:
        block = mine_block(miner_address)
        if block:
            return {"status": "success", "block": block}
        else:
            raise HTTPException(status_code=500, detail="Failed to mine block.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
