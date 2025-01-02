import json
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..services.message_handler import handle_transaction, handle_block

websocket_router = APIRouter()
logger = logging.getLogger("websocket")

@websocket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    logger.info("WebSocket connection attempt received.")
    await websocket.accept()
    is_closed = False
    try:
        logger.info("WebSocket connection established.")
        while True:
            try:
                data = await websocket.receive_text()
                logger.info(f"Message received: {data}")
                message = json.loads(data)

                # Determine the message type and handle accordingly
                msg_type = message.get("type")
                content = message.get("content")

                if msg_type == "transaction":
                    logger.info("Handling transaction message.")
                    response = handle_transaction(content)
                elif msg_type == "block":
                    logger.info("Handling block message.")
                    response = handle_block(content)
                else:
                    logger.warning(f"Unknown message type: {msg_type}")
                    response = {"type": "error", "content": "Unknown message type"}

                # Send the response back to the client
                await websocket.send_text(json.dumps(response))
            except WebSocketDisconnect:
                logger.info("WebSocket disconnected by client.")
                is_closed = True
                break
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON received: {e}")
                await websocket.send_text(
                    json.dumps({"type": "error", "content": "Invalid JSON format"})
                )
            except Exception as e:
                logger.error(f"Error processing message: {e}")
                await websocket.send_text(
                    json.dumps({"type": "error", "content": "Internal server error"})
                )
    except Exception as e:
        logger.error(f"Unexpected error in WebSocket handling: {e}")
    finally:
        if not is_closed:
            logger.info("Closing WebSocket connection.")
            try:
                await websocket.close()
            except Exception as e:
                logger.error(f"Error while closing WebSocket: {e}")
