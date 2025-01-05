from fastapi import APIRouter, HTTPException
from sallmon.sallmon_core.services.message_handler import process_message

# Initialize the router
router = APIRouter()

@router.post("/process-msg")
async def process_message_route(payload: dict):
    """
    API endpoint to process incoming messages.
    :param payload: The message payload.
    :return: Response from the message processing service.
    """
    try:
        # Process the message using the message handler
        response = await process_message(payload)
        return response
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
