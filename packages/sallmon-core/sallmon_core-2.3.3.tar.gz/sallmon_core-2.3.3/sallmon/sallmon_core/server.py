from typing import List, Dict
from fastapi import FastAPI, WebSocket, HTTPException, WebSocketDisconnect
from pydantic import BaseModel
import asyncio
import uvicorn

app = FastAPI()

# Active WebSocket connections
active_connections: Dict[str, WebSocket] = {}  # Keyed by peer_id or address


class MessagePayload(BaseModel):
    message_type: str
    message: str
    peer_id: str  # Unique identifier for the peer


# WebSocket Route
@app.websocket("/ws/{peer_id}")
async def websocket_route(websocket: WebSocket, peer_id: str):
    # Accept the WebSocket connection
    await websocket.accept()
    active_connections[peer_id] = websocket
    print(f"Peer {peer_id} connected. Total peers: {len(active_connections)}")

    try:
        while True:
            # Wait for a message from the client
            data = await websocket.receive_json()
            message_type = data.get("message_type", "UNKNOWN")
            print(f"Received from {peer_id}: {data}")

            if message_type == "PING":
                # Respond to heartbeat
                await websocket.send_json({"message_type": "PONG", "peer_id": peer_id})
            elif message_type == "MESSAGE":
                # Broadcast the message to other peers
                await broadcast_message(data)
    except WebSocketDisconnect:
        print(f"Peer {peer_id} disconnected")
        active_connections.pop(peer_id, None)


async def broadcast_message(message: dict):
    """Broadcast a message to all connected peers except the sender."""
    sender_peer_id = message.get("peer_id", "UNKNOWN")
    for peer_id, connection in active_connections.items():
        if peer_id != sender_peer_id:
            try:
                await connection.send_json(message)
            except Exception as e:
                print(f"Failed to send message to {peer_id}: {e}")


@app.post("/send-to-ws")
async def send_to_ws_route(payload: MessagePayload):
    if not active_connections:
        raise HTTPException(status_code=400, detail="No active WebSocket connections.")

    # Send the message to a specific peer or broadcast
    target_peer = payload.peer_id
    if target_peer in active_connections:
        await active_connections[target_peer].send_json(payload.dict())
    else:
        await broadcast_message(payload.dict())

    return {"status": "success", "message": "Message sent to WebSocket client(s)."}


# Helper for Heartbeat
async def ping_peers():
    """Periodically send PING messages to all peers."""
    while True:
        for peer_id, websocket in list(active_connections.items()):
            try:
                await websocket.send_json({"message_type": "PING", "peer_id": "server"})
            except WebSocketDisconnect:
                print(f"Peer {peer_id} disconnected during heartbeat")
                active_connections.pop(peer_id, None)
        await asyncio.sleep(10)  # Heartbeat interval


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(ping_peers())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1337)
