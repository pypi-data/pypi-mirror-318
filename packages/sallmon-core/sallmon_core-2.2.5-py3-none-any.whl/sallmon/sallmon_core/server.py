import asyncio
import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
import uvicorn
import httpx
import json
import websockets
from asyncio import Queue
from sallmon.sallmon_core.routes.peers import router as peers_router
from sallmon.sallmon_core.routes.mempool import router as mempool_router
from sallmon.sallmon_core.routes.utxo import router as utxo_router
from sallmon.sallmon_core.routes.mine import router as mine_router
from sallmon.sallmon_core.routes.blocks import router as blocks_router
from sallmon.sallmon_core.routes.peers import get_peers_list, broadcast

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

app = FastAPI()

# Active WebSocket connections and peer connections
active_connections = []
peer_connections = {}
message_queue = Queue()  # Shared queue for messages to be sent to WebSocket clients

# WebSocket Route
@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    """Handle incoming WebSocket connections."""
    await websocket.accept()
    active_connections.append(websocket)
    logging.info(f"New WebSocket connection: {websocket.client}")
    try:
        while True:
            data = await websocket.receive_text()
            logging.info(f"Received WebSocket message: {data}")
            for connection in active_connections:
                await connection.send_text(f"Broadcast: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        logging.info(f"WebSocket disconnected: {websocket.client}")

# HTTP Route to send a message to WebSocket clients
@app.post("/send-to-ws")
async def send_to_ws_route(payload: dict):
    """Broadcast a message to all WebSocket connections."""
    message = payload.get("message", "Default Message")
    logging.info(f"Broadcasting HTTP message: {message}")
    for connection in active_connections:
        try:
            await connection.send_text(f"Broadcast from HTTP: {message}")
        except Exception as e:
            logging.error(f"Error sending message to WebSocket: {e}")
    return {"status": "Message sent to WebSocket clients"}

async def connect_to_peer(peer_ip):
    """Connect to a peer WebSocket server."""
    ws_url = f"ws://{peer_ip}/ws"
    try:
        logging.info(f"Attempting to connect to peer: {ws_url}")
        async with websockets.connect(ws_url) as websocket:
            peer_connections[peer_ip] = websocket
            logging.info(f"Connected to peer: {ws_url}")
            while True:
                message = await websocket.recv()
                logging.info(f"Message received from peer {peer_ip}: {message}")
    except Exception as e:
        logging.error(f"Failed to connect to peer {peer_ip}: {e}")
        if peer_ip in peer_connections:
            del peer_connections[peer_ip]

async def manage_peers():
    """Periodically check and connect to peers."""
    while True:
        try:
            peers = await fetch_peers()
            logging.info(f"Fetched peers: {peers}")
            for peer_ip in peers:
                if peer_ip not in peer_connections:
                    asyncio.create_task(connect_to_peer(peer_ip))
        except Exception as e:
            logging.error(f"Error managing peers: {e}")
        await asyncio.sleep(10)  # Check every 10 seconds

async def fetch_peers():
    """Fetch peers from the `/get-peers` endpoint."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:1337/get-peers")
            response.raise_for_status()
            peers_data = response.json()
            logging.info(f"Peers fetched successfully: {peers_data}")
            return peers_data.get("peers", [])
    except httpx.RequestError as e:
        logging.error(f"An error occurred while requesting peers: {e}")
        return []
    except httpx.HTTPStatusError as e:
        logging.error(f"HTTP error while fetching peers: {e.response.text}")
        return []

@app.get("/get-peers")
async def get_peers():
    """Return the list of active WebSocket peers."""
    peers = await get_peers_list()
    logging.info(f"Active peers: {peers}")
    return peers

async def process_message_queue():
    """Process messages in the queue and send to all WebSocket connections."""
    while True:
        message = await message_queue.get()
        logging.debug(f"Processing message from queue: {message}")
        for connection in active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                logging.error(f"Error sending message to WebSocket client: {e}")
        message_queue.task_done()

# Include routes
app.include_router(peers_router)
app.include_router(mempool_router)
app.include_router(utxo_router)
app.include_router(mine_router)
app.include_router(blocks_router)

def start_server():
    """Start the FastAPI server and the peer management task."""
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(manage_peers())  # Start the peer management task
    loop.create_task(process_message_queue())  # Start the message processing task
    uvicorn.run(app, host="0.0.0.0", port=1337)
