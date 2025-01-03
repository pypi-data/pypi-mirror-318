from fastapi import APIRouter, HTTPException
from sallmon_core.services.blocks import validate_block, get_all_blocks
from sallmon_core.services.block_db import add_block, get_latest_block

router = APIRouter()

@router.post("/blocks")
def add_new_block(block: dict):
    """
    Add a new block to the blockchain.
    """
    is_valid, validation_message = validate_block(block)
    if not is_valid:
        raise HTTPException(status_code=400, detail=validation_message)

    try:
        add_block(block)
        return {"status": "success", "message": "Block added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding block: {e}")

@router.get("/blocks")
def view_all_blocks():
    """
    Retrieve all blocks from the blockchain.
    """
    blocks = get_all_blocks()
    return {"status": "success", "blocks": blocks}

@router.get("/blocks/latest")
def view_latest_block():
    """
    Retrieve the latest block from the blockchain.
    """
    block = get_latest_block()
    if block:
        return {"status": "success", "block": block}
    raise HTTPException(status_code=404, detail="No blocks found.")
