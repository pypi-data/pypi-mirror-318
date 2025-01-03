# sallmon_core/routes/mempool.py
from fastapi import APIRouter, HTTPException
from sallmon.sallmon_core.services.mempool import mempool

router = APIRouter()

@router.post("/mempool")
def add_transaction(transaction_id: str, transaction: dict):
    """
    Add a transaction to the mempool.
    """
    success = mempool.add_transaction(transaction_id, transaction)
    if success:
        return {"status": "success", "message": "Transaction added to mempool."}
    else:
        raise HTTPException(status_code=400, detail="Duplicate transaction.")

@router.get("/mempool")
def view_mempool():
    """
    View all transactions in the mempool.
    """
    transactions = mempool.get_transactions()
    return {"status": "success", "mempool": transactions}

@router.delete("/mempool")
def clear_mempool():
    """
    Clear all transactions in the mempool.
    """
    success = mempool.clear()
    if success:
        return {"status": "success", "message": "Mempool cleared."}
    else:
        raise HTTPException(status_code=500, detail="Failed to clear mempool.")
