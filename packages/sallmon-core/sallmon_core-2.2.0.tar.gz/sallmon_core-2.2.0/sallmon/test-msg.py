import asyncio
import httpx

BASE_URL = "http://96.70.45.233:1337/send-to-ws"
MESSAGE_TYPES = [
    {"type": "Chat", "content": {"text": "Hello, WebSocket!"}},
    {"type": "Block", "content": {"block_id": 12345, "data": "Block data"}},
    {"type": "Mempool", "content": {"transactions": ["tx1", "tx2"]}},
    {"type": "Command", "content": {"command": "RESTART"}},
    {"type": "Admin", "content": {"action": "UPDATE_CONFIG"}},
    {"type": "Metric", "content": {"metric": "CPU_USAGE", "value": "85%"}},
    {"type": "Sync", "content": {"sync_id": "abcd1234", "status": "active"}},
    {"type": "Transaction", "content": {"tx_id": "tx98765", "amount": 100.5}},
    {"type": "Alert", "content": {"level": "CRITICAL", "message": "Disk space low!"}},
    {"type": "Log", "content": {"log_id": "log001", "message": "System started"}}
]

async def send_message(client, message):
    try:
        response = await client.post(BASE_URL, json=message)
        print(f"Sent: {message['type']}, Response: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending message {message['type']}: {e}")

async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        for _ in range(10):  # Send 10 sets of messages rapidly
            for message in MESSAGE_TYPES:
                tasks.append(send_message(client, message))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
