from typing import List
from fastapi import FastAPI, WebSocket, HTTPException, WebSocketDisconnect
from pydantic import BaseModel
import uvicorn

# Import your routes
from sallmon.sallmon_core.routes.websocket import websocket_endpoint
from sallmon.sallmon_core.routes.api import api_endpoint
from sallmon.sallmon_core.routes.peers import router as peers_router
from sallmon.sallmon_core.routes.mempool import router as mempool_router
from sallmon.sallmon_core.routes.utxo import router as utxo_router
from sallmon.sallmon_core.routes.mine import router as mine_router
from sallmon.sallmon_core.routes.blocks import router as blocks_router

app = FastAPI()

# Active WebSocket connections
active_connections: List[WebSocket] = []

# Define MessagePayload for validation
class MessagePayload(BaseModel):
    message_type: str
    message: str

# WebSocket Route
@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    # Accept the WebSocket connection
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received WebSocket data: {data}")
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("WebSocket disconnected")
        active_connections.remove(websocket)

# HTTP Route to send a message to the WebSocket
@app.post("/send-to-ws")
async def send_to_ws_route(payload: MessagePayload):
    if not active_connections:
        raise HTTPException(status_code=400, detail="No active WebSocket connections.")

    # Broadcast the message to all connected WebSockets
    for websocket in active_connections:
        await websocket.send_json({
            "message_type": payload.message_type,
            "message": payload.message,
        })

    return {"status": "success", "message": "Message broadcasted to WebSocket clients."}

# Include routers
app.include_router(peers_router)
app.include_router(mempool_router)
app.include_router(utxo_router)
app.include_router(mine_router)
app.include_router(blocks_router)

# Server Start Function
def start_server():
    """Start the FastAPI server."""
    uvicorn.run(app, host="0.0.0.0", port=1337)
