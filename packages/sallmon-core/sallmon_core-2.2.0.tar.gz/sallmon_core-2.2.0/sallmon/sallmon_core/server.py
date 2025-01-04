from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
import uvicorn
from sallmon.sallmon_core.routes.websocket import websocket_endpoint
from sallmon.sallmon_core.routes.api import api_endpoint
from sallmon.sallmon_core.routes.peers import router as peers_router
from sallmon.sallmon_core.routes.mempool import router as mempool_router
from sallmon.sallmon_core.routes.utxo import router as utxo_router
from sallmon.sallmon_core.routes.mine import router as mine_router
from sallmon.sallmon_core.routes.blocks import router as blocks_router

app = FastAPI()

from sallmon.sallmon_core.routes.peers import get_peers_list, broadcast

# Store active WebSocket connections
active_connections = []

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    """Handle WebSocket connections."""
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast received messages to all connected peers
            for connection in active_connections:
                await connection.send_text(f"Broadcast: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)


@app.post("/send-to-ws")
async def send_to_ws_route(payload: dict):
    """Send a message to all WebSocket clients from an HTTP request."""
    message = payload.get("message", "Default Message")
    # Use the `broadcast` function from `routes/peers` for broadcasting
    responses = await broadcast({"message": message})
    return {"status": "Message sent to WebSocket clients", "responses": responses}


@app.get("/get-peers")
async def get_peers():
    """Return the list of active WebSocket peers using `routes/peers`."""
    # Use the `get_peers_list` function from `routes/peers`
    return await get_peers_list()


# Include various routes
app.include_router(peers_router)
app.include_router(mempool_router)
app.include_router(utxo_router)
app.include_router(mine_router)  # Add mining routes here
app.include_router(blocks_router)

def start_server():
    """Start the FastAPI server."""
    uvicorn.run(app, host="0.0.0.0", port=1337)
