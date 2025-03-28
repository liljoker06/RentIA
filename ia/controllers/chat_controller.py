from fastapi import HTTPException
from services.chat_service import process_user_message

def handle_chat(message: str):
    if not message or len(message) < 3:
        raise HTTPException(status_code=400, detail="Message trop court.")
    
    response = process_user_message(message)
    return {"response": response}
