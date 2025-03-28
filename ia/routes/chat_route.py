from fastapi import APIRouter, Request
from pydantic import BaseModel
from ai.retriever import retrieve_similar_rows
from ai.responder import (
    is_greeting,
    get_welcome_message,
    generate_response
)
from utils.web_search import search_web

chat_router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_name: str = ""  # Optionnel

@chat_router.post("/")
async def chat(request: ChatRequest):
    message = request.message
    user_name = request.user_name

    if is_greeting(message):
        return {"response": get_welcome_message(user_name)}

    results = retrieve_similar_rows(message)


    if results and results[0]["score"] >= 0.65:
        return {"response": generate_response(results, user_question=message)}

    web_results = search_web(message)
    if web_results:
        response = "Je n’ai pas trouvé de réponse claire dans mes données, mais voici ce que j’ai trouvé sur le web 🌐 :\n"
        for result in web_results:
            title = result.get("title", "Lien")
            href = result.get("href", "")
            response = f"{response}\n🔗 [{title}]({href})"
        return {"response": response}

    return {"response": "Désolé, je n’ai trouvé aucune information pertinente 😕."}
