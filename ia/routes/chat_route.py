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

# @chat_router.post("/")
# async def chat(request: ChatRequest):
#     message = request.message
#     user_name = request.user_name

#     if is_greeting(message):
#         return {"response": get_welcome_message(user_name)}

#     results = retrieve_similar_rows(message)


#     if results and results[0]["score"] >= 0.50:
#         return {"response": generate_response(results, user_question=message)}

#     web_results = search_web(message)
#     if web_results:
#         response = "Je n’ai pas trouvé de réponse claire dans mes données, mais voici ce que j’ai trouvé sur le web 🌐 :\n"
#         for result in web_results:
#             title = result.get("title", "Lien")
#             href = result.get("href", "")
#             response = f"{response}\n🔗 [{title}]({href})"
#         return {"response": response}

#     return {"response": "Désolé, je n’ai trouvé aucune information pertinente 😕."}


@chat_router.post("/")
async def chat(request: ChatRequest):
    message = request.message
    user_name = request.user_name

    if is_greeting(message):
        return {"response": get_welcome_message(user_name)}

    # Détecter la question spécifique
    if "logement le moins cher" in message.lower():
        return await get_cheapest_property()

    if "logement le plus cher" in message.lower():
        return await get_most_expensive_property()

    if "types de logements" in message.lower():
        return await get_property_types()

    if "top 5 des plus chers" in message.lower():
        return await get_top_5_most_expensive()

    if "top 5 des moins chers" in message.lower():
        return await get_top_5_cheapest()

    # Recherche des résultats généraux
    results = retrieve_similar_rows(message)

    if results and results[0]["score"] >= 0.50:
        return {"response": generate_response(results, user_question=message)}

    # Recherche web si pas de résultats pertinents
    web_results = search_web(message)
    if web_results:
        response = "Je n’ai pas trouvé de réponse claire dans mes données, mais voici ce que j’ai trouvé sur le web 🌐 :\n"
        for result in web_results:
            title = result.get("title", "Lien")
            href = result.get("href", "")
            response = f"{response}\n🔗 [{title}]({href})"
        return {"response": response}

    return {"response": "Désolé, je n’ai trouvé aucune information pertinente 😕."}

# Fonction pour nettoyer et convertir le prix
def parse_price(price_str: str) -> float:
    try:
        # Retirer le symbole de la devise et convertir en float
        return float(price_str.replace('$', '').replace('€', '').strip())
    except ValueError:
        return 0.0  # En cas d'erreur de conversion, retourner un prix de 0

# Fonction pour obtenir le logement le moins cher
async def get_cheapest_property():
    results = retrieve_similar_rows("logement le moins cher à Paris")
    if not results:
        return {"response": "Je n'ai pas trouvé de logement moins cher à Paris."}

    # Trier les résultats par prix en nettoyant et convertissant les valeurs
    cheapest = sorted(results, key=lambda x: parse_price(x["data"].get("price", 0)))[0]
    return {"response": generate_response([cheapest], user_question="logement le moins cher à Paris")}

# Fonction pour obtenir le logement le plus cher
async def get_most_expensive_property():
    results = retrieve_similar_rows("logement le plus cher à Paris")
    if not results:
        return {"response": "Je n'ai pas trouvé de logement plus cher à Paris."}

    # Trier les résultats par prix en nettoyant et convertissant les valeurs
    most_expensive = sorted(results, key=lambda x: parse_price(x["data"].get("price", 0)), reverse=True)[0]
    return {"response": generate_response([most_expensive], user_question="logement le plus cher à Paris")}

# Fonction pour obtenir le top 5 des logements les plus chers
async def get_top_5_most_expensive():
    results = retrieve_similar_rows("logements les plus chers à Paris")
    top_5 = sorted(results, key=lambda x: parse_price(x["data"].get("price", 0)), reverse=True)[:5]
    response = "Voici le top 5 des logements les plus chers à Paris :\n"
    for i, result in enumerate(top_5, start=1):
        response += f"{i}. {result['data']['name']} - {result['data']['price']} €\n"
    return {"response": response}

# Fonction pour obtenir le top 5 des logements les moins chers
async def get_top_5_cheapest():
    results = retrieve_similar_rows("logements les moins chers à Paris")
    top_5 = sorted(results, key=lambda x: parse_price(x["data"].get("price", 0)))[:5]
    response = "Voici le top 5 des logements les moins chers à Paris :\n"
    for i, result in enumerate(top_5, start=1):
        response += f"{i}. {result['data']['name']} - {result['data']['price']} €\n"
    return {"response": response}

# Fonction pour obtenir les types de logements disponibles
async def get_property_types():
    results = retrieve_similar_rows("types de logements à Paris")
    if not results:
        return {"response": "Je n'ai pas trouvé d'informations sur les types de logements à Paris."}

    # Compter les occurrences de chaque type de logement
    property_types = {}
    for result in results:
        room_type = result["data"].get("room_type", "Type pas préciser")
        property_types[room_type] = property_types.get(room_type, 0) + 1

    response = "Voici les types de logements disponibles à Paris :\n"
    for room_type, count in property_types.items():
        response += f"- {room_type.capitalize()} : {count}\n"
    return {"response": response}
