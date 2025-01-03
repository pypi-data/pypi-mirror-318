from fastapi import APIRouter, HTTPException

from fastapi import FastAPI, HTTPException
#from wallets import create_wallet, list_wallets, get_wallet, delete_wallet
from sallmon.sallmon_core.services.wallets import create_wallet, list_wallets, get_wallet, delete_wallet

#app = FastAPI()
router = APIRouter()


@router.post("/wallets")
def api_create_wallet(payload: dict):
    """Create a new wallet."""
    passphrase = payload.get("passphrase")
    if not passphrase:
        raise HTTPException(status_code=400, detail="Passphrase is required")
    try:
        wallet = create_wallet(passphrase)
        return {"status": "success", "wallet": wallet}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/wallets")
def api_list_wallets():
    """List all wallets."""
    return {"status": "success", "wallets": list_wallets()}

@router.get("/wallets/{wallet_id}")
def api_get_wallet(wallet_id: str):
    """Retrieve a wallet by ID."""
    wallet = get_wallet(wallet_id)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return {"status": "success", "wallet": wallet}

@router.delete("/wallets/{wallet_id}")
def api_delete_wallet(wallet_id: str):
    """Delete a wallet by ID."""
    if delete_wallet(wallet_id):
        return {"status": "success", "message": f"Wallet {wallet_id} deleted"}
    else:
        raise HTTPException(status_code=404, detail="Wallet not found")
