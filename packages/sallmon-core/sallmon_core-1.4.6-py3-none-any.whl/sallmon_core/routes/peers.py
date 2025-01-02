from fastapi import APIRouter, HTTPException
from ..services.peers import (
    add_peer,
    remove_peer,
    PEERS,
    save_dynamic_peers,
    handle_chat_message,
    handle_command,
    add_peer_to_db,
    load_peers_from_db,
)

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

    # Add the peer to the list and the database
    add_peer(peer_url)
    add_peer_to_db(peer_url)
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
        remove_peer(peer_url)
        save_dynamic_peers()
        return {"message": f"Peer {peer_url} removed successfully."}
    else:
        raise HTTPException(status_code=404, detail="Peer not found.")

@peer_router.post("/chat", tags=["Chat"])
async def chat_message_endpoint(chat: dict):
    """
    Send a chat message to all peers.
    """
    sender = chat.get("sender")
    message = chat.get("message")

    if not sender or not message:
        raise HTTPException(status_code=400, detail="Sender and message are required.")

    await handle_chat_message(sender, message)
    return {"message": f"Chat message from {sender} broadcasted successfully."}

@peer_router.post("/commands", tags=["Commands"])
async def command_endpoint(command: dict):
    """
    Send a command to all peers.
    """
    action = command.get("action")
    params = command.get("params", {})

    if not action:
        raise HTTPException(status_code=400, detail="Action is required in the command.")

    await handle_command(action, params)
    return {"message": f"Command '{action}' broadcasted successfully."}

@peer_router.get("/peers/load", tags=["Peers"])
async def load_peers():
    """
    Reload the list of peers from the database.
    """
    load_peers_from_db()
    return {"message": "Peers reloaded successfully.", "peers": PEERS}
