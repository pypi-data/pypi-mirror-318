import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
import uvicorn
import httpx
import websockets
from asyncio import Queue
from sallmon.sallmon_core.routes.peers import router as peers_router
from sallmon.sallmon_core.routes.mempool import router as mempool_router
from sallmon.sallmon_core.routes.utxo import router as utxo_router
from sallmon.sallmon_core.routes.mine import router as mine_router
from sallmon.sallmon_core.routes.blocks import router as blocks_router
from sallmon.sallmon_core.routes.peers import get_peers_list, broadcast

app = FastAPI()

# Active WebSocket connections and peer connections
active_connections = {}
peer_connections = {}
message_queue = Queue()  # Shared queue for messages to be sent to WebSocket clients


# Configure stdout-only logging with emojis
def log_to_console(message: str, emoji: str = "🌟"):
    """Prints logs to the console with emojis."""
    print(f"{emoji} {message}", flush=True)


# WebSocket Route
@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    """Handle incoming WebSocket connections with enhanced logging."""
    await websocket.accept()
    client_id = f"{websocket.client.host}:{websocket.client.port}"
    active_connections[client_id] = websocket
    log_to_console(f"🎉 New WebSocket connection: {client_id}")

    try:
        # Start heartbeat task
        heartbeat_task = asyncio.create_task(send_heartbeat(websocket, client_id))

        while True:
            data = await websocket.receive_text()
            log_to_console(f"💬 Received message from {client_id}: {data}")
            await broadcast_message(f"📡 {client_id} says: {data}", exclude=client_id)
    except WebSocketDisconnect:
        log_to_console(f"❌ Disconnected: {client_id}")
        active_connections.pop(client_id, None)
    finally:
        heartbeat_task.cancel()


# HTTP Route to send a message to WebSocket clients
@app.post("/send-to-ws")
async def send_to_ws_route(payload: dict):
    """Broadcast a message to all WebSocket connections."""
    message = payload.get("message", "Default Message")
    log_to_console(f"📢 HTTP Broadcast Message: {message}")
    await broadcast_message(f"🌐 Broadcast: {message}")
    return {"status": "Message sent to WebSocket clients"}


async def broadcast_message(message: str, exclude: str = None):
    """Broadcast a message to all active WebSocket connections."""
    log_to_console(f"🚀 Broadcasting message: {message}")
    for client_id, websocket in active_connections.items():
        if client_id == exclude:
            log_to_console(f"⏭️ Skipping {client_id} (excluded)")
            continue
        try:
            await websocket.send_text(message)
            log_to_console(f"✅ Sent to {client_id}: {message}")
        except Exception as e:
            log_to_console(f"⚠️ Error sending to {client_id}: {e}")
            active_connections.pop(client_id, None)
            log_to_console(f"🧹 Cleaned up {client_id}")


async def send_heartbeat(websocket: WebSocket, client_id: str):
    """Send periodic heartbeat messages to the WebSocket client."""
    try:
        while True:
            await asyncio.sleep(10)  # 10-second interval for heartbeat
            await websocket.send_text("PING")
            log_to_console(f"💓 Heartbeat sent to {client_id}")
    except Exception as e:
        log_to_console(f"💔 Heartbeat failed for {client_id}: {e}")
        active_connections.pop(client_id, None)
        log_to_console(f"🧹 Removed {client_id} after failed heartbeat")


async def connect_to_peer(peer_ip):
    """Connect to a peer WebSocket server."""
    ws_url = f"ws://{peer_ip}/ws"
    try:
        log_to_console(f"🌐 Attempting to connect to peer: {ws_url}")
        async with websockets.connect(ws_url) as websocket:
            peer_connections[peer_ip] = websocket
            log_to_console(f"🔗 Connected to peer: {ws_url}")
            while True:
                message = await websocket.recv()
                log_to_console(f"💌 Message received from peer {peer_ip}: {message}")
    except Exception as e:
        log_to_console(f"⚠️ Failed to connect to peer {peer_ip}: {e}")
        if peer_ip in peer_connections:
            del peer_connections[peer_ip]


async def manage_peers():
    """Periodically check and connect to peers."""
    while True:
        try:
            peers = await fetch_peers()
            log_to_console(f"🧩 Fetched peers: {peers}")
            for peer_ip in peers:
                if peer_ip not in peer_connections:
                    asyncio.create_task(connect_to_peer(peer_ip))
        except Exception as e:
            log_to_console(f"⚠️ Error managing peers: {e}")
        await asyncio.sleep(10)  # Check every 10 seconds


async def fetch_peers():
    """Fetch peers from the `/get-peers` endpoint."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:1337/get-peers")
            response.raise_for_status()
            peers_data = response.json()
            log_to_console(f"✅ Peers fetched successfully: {peers_data}")
            return peers_data.get("peers", [])
    except httpx.RequestError as e:
        log_to_console(f"❌ Error requesting peers: {e}")
        return []
    except httpx.HTTPStatusError as e:
        log_to_console(f"❌ HTTP error fetching peers: {e.response.text}")
        return []


@app.get("/get-peers")
async def get_peers():
    """Return the list of active WebSocket peers."""
    peers = await get_peers_list()
    log_to_console(f"📋 Active peers: {peers}")
    return peers


async def process_message_queue():
    """Process messages in the queue and send to all WebSocket connections."""
    while True:
        message = await message_queue.get()
        log_to_console(f"📬 Processing queued message: {message}")
        await broadcast_message(message)
        message_queue.task_done()
        log_to_console(f"✅ Finished processing queued message: {message}")


def check_port(port):
    """Check if the port is already in use."""
    import socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
    except Exception as e:
        log_to_console(f"⚠️ Error checking port: {e}")
        return False


def start_server():
    """Start the FastAPI server and the peer management task."""
    if check_port(1337):
        log_to_console("❌ Port 1337 is already in use. Please stop the existing process or use a different port.")
        return

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(manage_peers())  # Start the peer management task
    loop.create_task(process_message_queue())  # Start the message processing task

    try:
        log_to_console("🔥 Starting FastAPI server...")
        uvicorn.run(app, host="0.0.0.0", port=1337)
    except Exception as e:
        log_to_console(f"❌ Error running server: {e}")
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


# Include routes
app.include_router(peers_router)
app.include_router(mempool_router)
app.include_router(utxo_router)
app.include_router(mine_router)
app.include_router(blocks_router)
