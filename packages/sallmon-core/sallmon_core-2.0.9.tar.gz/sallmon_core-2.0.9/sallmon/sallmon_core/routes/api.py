
from sallmon.sallmon_core.services.message_handler import process_message

async def api_endpoint(payload: dict):
    return await process_message(payload)
