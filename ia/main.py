from fastapi import FastAPI
from routes.chat_route import chat_router


app = FastAPI(
    title="RenalIA 🧠",
    description="Une IA avec laquelle discuter et poser des questions basées sur les données CSV 📊",
    version="0.1.0"
)

# inclusion des routes
app.include_router(chat_router, prefix="/chat", tags=["discussion"])


# Lancement de l'application
async def root():
     return {"message": "Bienvenue sur RenalIA 🚀. Utilise /chat pour discuter avec l'IA."}