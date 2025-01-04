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
@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    """Handle incoming WebSocket connections."""
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            logging.info(f"Received WebSocket data: {data}")
            # Broadcast to all connected clients
            for connection in active_connections:
                await connection.send_text(f"Broadcast: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        logging.info("WebSocket disconnected")

@app.post("/send-to-ws")
async def send_to_ws_route(payload: dict):
    """Broadcast a message to all WebSocket connections."""
    message = payload.get("message", "Default Message")
    # Broadcast to all WebSocket clients
    for connection in active_connections:
        await connection.send_text(f"Broadcast from HTTP: {message}")
    return {"status": "Message sent to WebSocket clients"}

async def connect_to_peer(peer_ip):
    """Connect to a peer WebSocket server."""
    ws_url = f"ws://{peer_ip}/ws"
    try:
        logging.info(f"Attempting to connect to peer at {ws_url}")
        async with websockets.connect(ws_url) as websocket:
            peer_connections[peer_ip] = websocket
            logging.info(f"Connected to peer at {ws_url}")
            while True:
                message = await websocket.recv()
                logging.info(f"Message from peer {peer_ip}: {message}")
    except Exception as e:
        logging.error(f"Failed to connect to peer {peer_ip}: {e}")
        if peer_ip in peer_connections:
            del peer_connections[peer_ip]

async def manage_peers():
    """Periodically check and connect to peers."""
    while True:
        try:
            # Replace with actual endpoint to get peers
            peers = await fetch_peers()
            for peer_ip in peers:
                if peer_ip not in peer_connections:
                    asyncio.create_task(connect_to_peer(peer_ip))
        except Exception as e:
            logging.error(f"Error managing peers: {e}")
        await asyncio.sleep(10)


import httpx
import logging

async def fetch_peers():
    """Fetch peers from the `/get-peers` endpoint."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:1337/get-peers")
            response.raise_for_status()
            peers_data = response.json()
            # Assuming the endpoint returns a list of peers in the "peers" key
            return peers_data.get("peers", [])
    except httpx.RequestError as e:
        logging.error(f"An error occurred while requesting peers: {e}")
        return []
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error while fetching peers: {e.response.text}")
        return []


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
