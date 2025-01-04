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

# WebSocket Route
@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)

# HTTP Route to send a message to the WebSocket
@app.post("/send-to-ws")
async def send_to_ws_route(payload: dict):
    return await api_endpoint(payload)

# Include various routes
app.include_router(peers_router)
app.include_router(mempool_router)
app.include_router(utxo_router)
app.include_router(mine_router)  # Add mining routes here
app.include_router(blocks_router)

def start_server():
    """Start the FastAPI server."""
    uvicorn.run(app, host="0.0.0.0", port=1337)
