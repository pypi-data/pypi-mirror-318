from fastapi import APIRouter, HTTPException
from sallmon.sallmon_core.services.utxos import add_utxo, get_utxos, spend_utxo
from pydantic import BaseModel

router = APIRouter()

@router.get("/utxos")
def api_get_utxos(address: str = None):
    """Retrieve UTXOs, optionally filtered by address."""
    utxos = get_utxos(address)
    return {"status": "success", "utxos": utxos}

# Define UTXO data model
class UTXO(BaseModel):
    txid: str
    index: int
    address: str
    amount: float

@router.post("/utxos")
async def api_add_utxo(utxo: UTXO):
    """Add a UTXO to the database."""
    try:
        add_utxo(utxo.txid, utxo.index, utxo.address, utxo.amount)
        return {"status": "success", "message": "UTXO added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/utxos/{id}/spend")
def api_spend_utxo(id: int):
    """Mark a UTXO as spent."""
    try:
        spend_utxo(id)
        return {"status": "success", "message": "UTXO spent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define a Pydantic model for the request payload
class SpendUTXORequest(BaseModel):
    txid: str
    index: int
    address: str
    amount: float

@router.post("/spend-utxo")
def api_spend_utxo(request: SpendUTXORequest):
    """Spend a UTXO."""
    success = spend_utxo(request.txid, request.index, request.address, request.amount)
    if success:
        return {"status": "success", "message": "UTXO spent successfully."}
    else:
        raise HTTPException(status_code=404, detail="UTXO not found or already spent.")
