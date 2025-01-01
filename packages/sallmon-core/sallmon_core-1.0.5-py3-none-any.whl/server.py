# server.py
import logging
from fastapi import FastAPI
from routes.api import api_router
from routes.websocket import websocket_router
from services.database import initialize_db  # Import the database initialization function
import uvicorn  # Import uvicorn here

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Initialize the database and create tables if they don't exist
initialize_db()

# Create the FastAPI app
app = FastAPI()

# Include API and WebSocket routes
app.include_router(api_router)
app.include_router(websocket_router)

def start_server():
    """Start the FastAPI server using Uvicorn."""
    uvicorn.run("server:app", host="0.0.0.0", port=1337, reload=True)
