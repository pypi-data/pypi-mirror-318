from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
from sallmon_core.routes.wallet import router as wallet_router
from sallmon_core.routes.websocket import websocket_endpoint
from sallmon_core.routes.api import api_endpoint
from sallmon_core.routes.peers import router as peers_router

app = FastAPI()

# WebSocket Route
@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)

# HTTP Route to send a message to the WebSocket
@app.post("/send-to-ws")
async def send_to_ws_route(payload: dict):
    return await api_endpoint(payload)


# Peering Routes
app.include_router(peers_router)


app.include_router(wallet_router) #, prefix="/wallets")

from sallmon_core.routes.mempool import router as mempool_router

# Include mempool routes
app.include_router(mempool_router)

from sallmon_core.routes.utxo import router as utxo_router

# Include UTXO routes
app.include_router(utxo_router)

from sallmon_core.routes.mine import router as mine_router

# Include UTXO routes
app.include_router(mine_router)


from sallmon_core.routes.blocks import router as blocks_router

app.include_router(blocks_router)  #, prefix="/blocks")

from sallmon_core.server import app  # Import the FastAPI app

def start_server():
    """Start the FastAPI server."""
    uvicorn.run(app, host="0.0.0.0", port=1337)
