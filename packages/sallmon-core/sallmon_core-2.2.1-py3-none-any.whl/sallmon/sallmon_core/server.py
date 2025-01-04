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
from asyncio import Queue

# Store active WebSocket connections
active_connections = []
message_queue = Queue()  # Shared queue for messages to be sent to WebSocket clients

async def process_message_queue():
    """Continuously send messages from the queue to all active WebSocket connections."""
    while True:
        message = await message_queue.get()
        for connection in active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                print(f"Error sending message: {e}")
                active_connections.remove(connection)

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    """Handle WebSocket connections."""
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            # WebSocket client message handling (optional if no two-way messaging is needed)
            data = await websocket.receive_text()
            print(f"Received from WebSocket client: {data}")
            await message_queue.put(f"Echo: {data}")
    except WebSocketDisconnect:
        print("WebSocket disconnected")
        active_connections.remove(websocket)

@app.post("/send-to-ws")
async def send_to_ws_route(payload: dict):
    """Handle HTTP requests to broadcast a message to WebSocket clients."""
    message = payload.get("message", "Default Message")
    await message_queue.put(f"Broadcast: {message}")
    return {"status": "Message added to WebSocket queue"}


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
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(process_message_queue())  # Start the message processing task
