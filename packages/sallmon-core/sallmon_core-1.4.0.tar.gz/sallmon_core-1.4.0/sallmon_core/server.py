import logging
import asyncio
import os
from pathlib import Path
from fastapi import FastAPI
from .routes.api import api_router
from .routes.websocket import websocket_router
from .routes.peers import peer_router
from .services.peers import sync_blockchain, periodic_peer_validation, broadcast_new_peer
from .services.database import initialize_db
import uvicorn
import socket
import sqlite3

# Ensure the logs directory exists
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Enhanced logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "server.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("server")

# Initialize database
initialize_db()

# Create FastAPI app
app = FastAPI()

# Include routers
app.include_router(api_router)
app.include_router(websocket_router)
app.include_router(peer_router)

def get_node_ip():
    """Get the IP address of the current node."""
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        logger.info(f"🌐 Node IP address determined: {ip}")
        return ip
    except Exception as e:
        logger.error(f"❌ Failed to determine node IP address: {e}")
        return "127.0.0.1"

def add_peer_to_db(peer_url):
    """Add a peer to the database, ensuring no duplicates."""
    db_path = os.path.expanduser("~/.sallmon/blockchain.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS peers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                peer_url TEXT UNIQUE NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT OR IGNORE INTO peers (peer_url)
            VALUES (?)
        ''', (peer_url,))
        conn.commit()
        logger.info(f"✅ Peer {peer_url} added to the database.")
    except Exception as e:
        logger.error(f"❌ Failed to add peer {peer_url} to the database: {e}")
    finally:
        conn.close()

async def announce_self_on_startup():
    """Announce the current node to the network."""
    node_ip = get_node_ip()
    node_url = f"ws://{node_ip}:1337/ws"
    add_peer_to_db(node_url)  # Add the current node to the local database
    await broadcast_new_peer(node_url)  # Broadcast the node to the network
    logger.info(f"📢 Node announced on startup: {node_url}")

# Blockchain synchronization at startup
@app.on_event("startup")
async def startup_event():
    """Initialize services and synchronize blockchain at startup."""
    logger.info("🚀 Starting server and initializing services...")

    # Announce the current node
    logger.info("📢 Announcing the current node to the network...")
    await announce_self_on_startup()

    # Sync the blockchain with peers
    logger.info("🔄 Synchronizing blockchain with peers...")
    sync_blockchain()

    # Start periodic peer validation
    logger.info("🔍 Starting periodic peer validation...")
    asyncio.create_task(periodic_peer_validation(interval=60))

    # Start periodic blockchain sync
    logger.info("🔄 Starting periodic blockchain synchronization...")
    asyncio.create_task(periodic_blockchain_sync(interval=120))

async def periodic_blockchain_sync(interval: int):
    """Periodically synchronize the blockchain with peers."""
    while True:
        logger.info("🔄 Performing periodic blockchain synchronization...")
        sync_blockchain()
        await asyncio.sleep(interval)

def start():
    """Entry point for sallmon-server command."""
    logger.info("🚀 Starting the sallmon-server...")
    uvicorn.run(app, host="0.0.0.0", port=1337, log_level="info")

if __name__ == "__main__":
    start()
