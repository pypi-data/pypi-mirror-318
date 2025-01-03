from fastapi import WebSocket

from sallmon_core.services.message_handler import process_message

connected_clients = set()

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            response = await process_message(data)
            await websocket.send_json(response)
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
