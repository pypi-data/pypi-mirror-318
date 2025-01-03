from fastapi import APIRouter, HTTPException
from sallmon_core.services.peers import add_peer, get_peers

router = APIRouter()

@router.post("/register-peer")
async def register_peer(peer: dict):
    peer_ip = peer.get("ip")
    if not peer_ip:
        raise HTTPException(status_code=400, detail="IP address is required")
    add_peer(peer_ip)
    return {"status": "success", "message": f"Peer {peer_ip} added"}

@router.get("/get-peers")
async def get_peers_list():
    return {"peers": get_peers()}

from fastapi import APIRouter
from sallmon_core.services.peers import broadcast_message

@router.post("/broadcast")
async def broadcast(payload: dict):
    responses = broadcast_message(payload)
    return {"status": "broadcasted", "responses": responses}
