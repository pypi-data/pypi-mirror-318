from fastapi import APIRouter, HTTPException
from ..services.peers import add_peer, PEERS, save_dynamic_peers

from fastapi import APIRouter, HTTPException
#from sallmon_core.services.peers import add_peer, PEERS, save_dynamic_peers

# Initialize APIRouter
peer_router = APIRouter()

@peer_router.get("/peers", tags=["Peers"])
async def get_peers():
    """
    Get the list of all known peers.
    """
    return {"peers": PEERS}

@peer_router.post("/peers", tags=["Peers"])
async def add_peer_endpoint(peer: dict):
    """
    Add a new peer to the network.
    """
    peer_url = peer.get("peer")
    if not peer_url:
        raise HTTPException(status_code=400, detail="Peer URL is required.")
    
    add_peer(peer_url)
    return {"message": f"Peer {peer_url} added successfully."}

@peer_router.delete("/peers", tags=["Peers"])
async def remove_peer_endpoint(peer: dict):
    """
    Remove a peer from the network.
    """
    peer_url = peer.get("peer")
    if not peer_url:
        raise HTTPException(status_code=400, detail="Peer URL is required.")
    
    if peer_url in PEERS:
        PEERS.remove(peer_url)
        save_dynamic_peers()
        return {"message": f"Peer {peer_url} removed successfully."}
    else:
        raise HTTPException(status_code=404, detail="Peer not found.")
