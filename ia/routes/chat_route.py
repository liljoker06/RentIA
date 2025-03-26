from fastapi import APIRouter
from pydantic import BaseModel
from controllers.chat_controller import handle_chat

chat_router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@chat_router.post("/")
async def chat(request: ChatRequest):
    # Appelle le contrôleur qui gère l'IA
    return handle_chat(request.message)
