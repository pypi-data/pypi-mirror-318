import logging
import asyncio
from fastapi import FastAPI
from .routes.api import api_router
from .routes.websocket import websocket_router
from .routes.peers import peer_router
from .services.peers import sync_blockchain, periodic_peer_validation
from .services.database import initialize_db
import uvicorn

# Enhanced logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("logs/server.log"),
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

# Blockchain synchronization at startup
@app.on_event("startup")
async def startup_event():
    """Initialize services and synchronize blockchain at startup."""
    logger.info("Starting server and initializing services...")

    # Sync the blockchain with peers
    logger.info("Synchronizing blockchain with peers...")
    sync_blockchain()

    # Start periodic peer validation
    logger.info("Starting periodic peer validation...")
    asyncio.create_task(periodic_peer_validation(interval=60))

    # Start periodic blockchain sync
    logger.info("Starting periodic blockchain synchronization...")
    asyncio.create_task(periodic_blockchain_sync(interval=120))


async def periodic_blockchain_sync(interval: int):
    """Periodically synchronize the blockchain with peers."""
    while True:
        logger.info("Performing periodic blockchain synchronization...")
        sync_blockchain()
        await asyncio.sleep(interval)


def start():
    """Entry point for sallmon-server command."""
    logger.info("Starting the sallmon-server...")
    uvicorn.run(app, host="0.0.0.0", port=1337, log_level="info")


if __name__ == "__main__":
    start()
