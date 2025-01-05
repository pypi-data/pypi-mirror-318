from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse, HTMLResponse
from threading import Thread
import asyncio
import websockets
import requests
import logging
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

# Store active WebSocket connections
connections = []

# Hardcoded peer WebSocket URL (replace with actual peer address)
PEER_WS_URL = "ws://172.234.207.57:1337/ws"

# Configure logging to only output to the console (stdout)
logging.basicConfig(
    level=logging.DEBUG,  # Set logging to DEBUG for detailed output
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()  # Log only to the console
    ],
)

PING_INTERVAL = 30  # Interval for sending pings to clients

# Forward message to processing server
async def forward_to_processor(message):
    """Forward WebSocket message to the processing server."""
    try:
        logging.debug(f"Forwarding message to processor: {message}")
        response = requests.post("http://127.0.0.1:1339/process-message", json=message)
        if response.status_code == 200:
            logging.info("Message processed successfully by the server.")
        else:
            logging.warning(f"Failed to process message. Server responded with status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Error forwarding message to server: {e}")

# WebSocket Route
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Handle incoming WebSocket connections."""
    await websocket.accept()
    connections.append(websocket)
    logging.info(f"New WebSocket connection established. Total connections: {len(connections)}")
    
    try:
        while True:
            try:
                # Wait for a message with a timeout for ping-pong
                data = await asyncio.wait_for(websocket.receive_text(), timeout=PING_INTERVAL)
                logging.debug(f"Received message from client: {data}")
                
                # Forward message to processor
                await forward_to_processor({"message": data})

                # Broadcast the message to all connected clients
                for conn in connections:
                    if conn != websocket:
                        await conn.send_text(f"Broadcast: {data}")
                        logging.debug(f"Broadcasted message to a client: {data}")
            except asyncio.TimeoutError:
                # Timeout: send a ping
                await websocket.send_text("ping")
                logging.debug("Ping sent to client to keep connection alive.")
    except WebSocketDisconnect:
        connections.remove(websocket)
        logging.warning(f"WebSocket client disconnected. Remaining connections: {len(connections)}")
    except Exception as e:
        logging.error(f"Unexpected error during WebSocket communication: {e}")

class Message(BaseModel):
    message_type: str
    message: Dict
    peer_id: str

@app.post("/send-to-ws")
async def send_to_ws(payload: Message):
    """Send a message to connected WebSocket clients and the peer."""
    message = payload.message
    logging.info(f"Received message via /send-to-ws: {message}")

    # Broadcast to local WebSocket clients
    for conn in connections:
        await conn.send_text(f"Message from /send-to-ws: {message}")
        logging.debug(f"Message sent to local WebSocket client: {message}")

    # Send to the peer
    try:
        async with websockets.connect(PEER_WS_URL) as websocket:
            await websocket.send(message)
            logging.info(f"Message sent to peer {PEER_WS_URL}: {message}")
    except Exception as e:
        logging.error(f"Failed to send message to peer {PEER_WS_URL}: {e}")

    return {"status": "success", "message": "Message processed successfully"}

@app.get("/")
async def stats():
    """Basic stats page."""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>WebSocket Stats</title>
    </head>
    <body>
        <h1>WebSocket Server Stats</h1>
        <p>Connected Clients: {len(connections)}</p>
        <p>Peer URL: {PEER_WS_URL}</p>
    </body>
    </html>
    """
    return HTMLResponse(html_content)

async def connect_to_peer():
    """Continuously try to connect to the peer WebSocket server."""
    while True:
        try:
            async with websockets.connect(PEER_WS_URL) as websocket:
                logging.info(f"Connected to peer: {PEER_WS_URL}")
                while True:
                    await asyncio.sleep(1)  # Keep the connection alive
        except Exception as e:
            logging.warning(f"Failed to connect to peer {PEER_WS_URL}: {e}")
            await asyncio.sleep(5)  # Retry every 5 seconds

def start_peer_connection():
    """Start the peer connection in a separate thread."""
    asyncio.run(connect_to_peer())

# Start the peer connection thread
Thread(target=start_peer_connection, daemon=True).start()
