import asyncio
import websockets
import logging
import json

# Setup Logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("WebSocketTest")

# Configuration
PEER_URL = "ws://172.234.207.57:1337/ws"
#PEER_URL = "ws://:1337/ws"
TEST_MESSAGE = {"type": "hello", "content": "Hello, World"}

async def test_websocket_connection():
    try:
        logger.info(f"Connecting to WebSocket peer: {PEER_URL}")
        async with websockets.connect(PEER_URL) as websocket:
            logger.info("Connection established!")

            # Send the test message
            message = json.dumps(TEST_MESSAGE)
            logger.info(f"Sending message: {message}")
            await websocket.send(message)

            # Wait for a response
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=5)
                logger.info(f"Received response: {response}")
            except asyncio.TimeoutError:
                logger.warning("No response received within the timeout period.")
    except websockets.ConnectionClosed as e:
        logger.error(f"WebSocket connection closed unexpectedly: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

# Run the WebSocket test
if __name__ == "__main__":
    asyncio.run(test_websocket_connection())
