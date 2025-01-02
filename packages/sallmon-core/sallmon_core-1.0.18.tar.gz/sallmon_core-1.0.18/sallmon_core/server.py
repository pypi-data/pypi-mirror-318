import logging
from fastapi import FastAPI
from .routes.api import api_router
from .routes.websocket import websocket_router
from .routes.peers import peer_router
from .services.database import initialize_db
import uvicorn

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Initialize database
initialize_db()

# Create FastAPI app
app = FastAPI()
app.include_router(api_router)
app.include_router(websocket_router)
app.include_router(peer_router)

def start():
    """Entry point for sallmon-server command."""
    uvicorn.run(app, host="0.0.0.0", port=1337)

if __name__ == "__main__":
    start()
