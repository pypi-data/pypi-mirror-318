
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse, HTMLResponse
from threading import Thread
import asyncio
import websockets
import requests

app = FastAPI()

# Store active WebSocket connections
connections = []

# Hardcoded peer WebSocket URL (replace with actual peer address)
PEER_WS_URL = "ws://172.234.207.57:1337/ws"

import requests

import logging

# Configure logging to only output to the console (stdout)
logging.basicConfig(
    level=logging.INFO,  # Adjust the logging level as needed
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()  # Log only to the console
    ],
)

# Forward message to processing server
async def forward_to_processor(message):
    """Forward WebSocket message to the processing server."""
    try:
        response = requests.post("http://127.0.0.1:1339/process-message", json=message)
        if response.status_code == 200:
            print("Message processed successfully by the server.")
        else:
            print(f"Failed to process message. Server responded with status code: {response.status_code}")
    except Exception as e:
        print(f"Error forwarding message to server: {e}")

# WebSocket Route
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """Handle incoming WebSocket connections."""
    await websocket.accept()
    connections.append(websocket)
    print("New WebSocket connection established.")
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received from WebSocket client: {data}")

            # Forward to processing server
            await forward_to_processor({"message": data})

            # Broadcast the message to all connected clients
            for conn in connections:
                if conn != websocket:
                    await conn.send_text(f"Broadcast: {data}")
    except WebSocketDisconnect:
        connections.remove(websocket)
        print("WebSocket client disconnected.")

from pydantic import BaseModel

#class Message(BaseModel):
#    message: str

from typing import Dict

class Message(BaseModel):
    message_type: str
    message: Dict  # Update from str to Dict
    peer_id: str

@app.post("/send-to-ws")
async def send_to_ws(payload: Message):
    """Send a message to connected WebSocket clients and the peer."""
    message = payload.message

    # Broadcast to local WebSocket clients
    for conn in connections:
        await conn.send_text(f"Message from /send-to-ws: {message}")
    print(f"Sent to local WebSocket clients: {message}")

    # Send to the peer
    try:
        async with websockets.connect(PEER_WS_URL) as websocket:
            await websocket.send(message)
            print(f"Sent to peer: {PEER_WS_URL}")
    except Exception as e:
        print(f"Failed to send to peer {PEER_WS_URL}: {e}")

#    return JSONResponse({"status": "Message sent", "message": message})
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
                print(f"Connected to peer: {PEER_WS_URL}")
                while True:
                    await asyncio.sleep(1)  # Keep the connection alive
        except Exception as e:
            print(f"Failed to connect to peer {PEER_WS_URL}: {e}")
            await asyncio.sleep(5)  # Retry every 5 seconds

import requests

import logging

async def forward_to_processor(message):
    """Forward WebSocket message to the processing server."""
    try:
        logging.info(f"Forwarding message to processor: {message}")
        response = requests.post("http://127.0.0.1:1339/process-msg", json=message)
        if response.status_code == 200:
            logging.info(f"Message processed successfully: {response.json()}")
        else:
            logging.warning(
                f"Failed to process message. Server responded with status code: {response.status_code}"
            )
    except Exception as e:
        logging.error(f"Error forwarding message to server: {e}")


def start_peer_connection():
    """Start the peer connection in a separate thread."""
    asyncio.run(connect_to_peer())

# Start the peer connection thread
Thread(target=start_peer_connection, daemon=True).start()
