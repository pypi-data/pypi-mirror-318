import json
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..services.peers import add_peer, PEER_STATUSES
from ..services.message_handler import handle_transaction, handle_block, handle_command

websocket_router = APIRouter()
logger = logging.getLogger("websocket")

@websocket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for handling peer communication, heartbeats, chat, and admin commands.
    """
    logger.info("WebSocket connection attempt received.")
    await websocket.accept()
    peer_address = f"ws://{websocket.client.host}:{websocket.client.port}/ws"
    is_closed = False

    try:
        # Add the peer on connection
        logger.info(f"WebSocket connection established with peer: {peer_address}")
        add_peer(peer_address)

        while True:
            try:
                # Receive and parse WebSocket message
                data = await websocket.receive_text()
                logger.info(f"Message received from {peer_address}: {data}")
                message = json.loads(data)

                msg_type = message.get("type")
                content = message.get("content")

                if msg_type == "transaction":
                    logger.info("Handling transaction message.")
                    response = handle_transaction(content)
                elif msg_type == "block":
                    logger.info("Handling block message.")
                    response = handle_block(content)
                elif msg_type == "ping":
                    logger.info("Heartbeat ping received. Sending pong.")
                    PEER_STATUSES[peer_address] = "online"
                    response = {"type": "pong", "content": "Alive"}
                elif msg_type == "chat":
                    logger.info(f"Chat message received from {peer_address}: {content}")
                    response = {"type": "chat_ack", "content": "Message received"}
                elif msg_type == "command":
                    logger.info(f"Admin command received: {content}")
                    response = handle_command(content)
                else:
                    logger.warning(f"Unknown message type: {msg_type}")
                    response = {"type": "error", "content": "Unknown message type"}

                # Send the response
                await websocket.send_text(json.dumps(response))
            except WebSocketDisconnect:
                logger.info(f"WebSocket disconnected by peer: {peer_address}")
                is_closed = True
                PEER_STATUSES[peer_address] = "offline"
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
            logger.info(f"Closing WebSocket connection for peer: {peer_address}")
            try:
                await websocket.close()
            except Exception as e:
                logger.error(f"Error while closing WebSocket: {e}")
