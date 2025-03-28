from typing import List, Dict
import re

def generate_response(results: List[Dict], user_question: str = "") -> str:
    if not results:
        return "Hmm... j’ai fouillé dans les données, mais je n’ai rien trouvé qui corresponde vraiment à ta question 😕."

    top_result = results[0]
    logement = top_result['data']
    score = top_result['score']

    # Infos principales
    name = logement.get("name", "un logement sans nom")
    quartier = logement.get("neighbourhood", "un quartier inconnu")
    room_type = logement.get("room_type", "un type inconnu")
    prix = logement.get("price", "un prix inconnu")

    # Moyenne des prix
    prices = [row["data"].get("price", 0) for row in results if isinstance(row["data"].get("price", 0), (int, float))]
    avg_price = round(sum(prices) / len(prices), 2) if prices else "?"

    # Analyse de tendance
    if isinstance(prix, (int, float)) and isinstance(avg_price, (int, float)):
        if prix > avg_price:
            tendance = "💸 Ce logement est un peu plus cher que la moyenne."
        elif prix < avg_price:
            tendance = "🤑 Ce logement est une bonne affaire, moins cher que la moyenne !"
        else:
            tendance = "💰 Ce logement est exactement dans la moyenne des prix."
    else:
        tendance = ""

    # Autres infos disponibles
    nights = logement.get("minimum_nights")
    reviews = logement.get("number_of_reviews")
    availability = logement.get("availability_365")
    latitude = logement.get("latitude")
    longitude = logement.get("longitude")
    available = logement.get("available")
    last_date = logement.get("date")

    maps_link = ""
    if latitude and longitude:
        maps_link = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

    # 🧠 Génération de la réponse naturelle
    response = f"🔍 En réponse à ta question : « {user_question} », voici ce que j’ai trouvé 👇\n\n"
    response += f"🏠 *{name}* est un logement situé à **{quartier}**.\n"
    response += f"C’est un type de logement : **{room_type}**, proposé à environ **{prix} €**.\n"
    response += f"\n📊 Le prix moyen des logements similaires est de **{avg_price} €**.\n"
    response += f"{tendance}\n"

    if nights:
        response += f"🛏️ Séjour minimum : {nights} nuit{'s' if nights > 1 else ''}.\n"
    if reviews:
        response += f"⭐ Nombre d’avis : {reviews}.\n"
    if availability:
        response += f"📅 Disponibilité annuelle : {availability} jours/an.\n"
    if available is not None:
        response += f"📌 Actuellement disponible : {'✅ Oui' if available else '❌ Non'}.\n"
    if last_date:
        response += f"📆 Dernière mise à jour de disponibilité : {last_date}.\n"
    if maps_link:
        response += f"📍 [Voir l’emplacement sur Google Maps]({maps_link})\n"

    response += f"\n🤖 (Indice de pertinence : {round(score * 100)}%)\n"
    response += "\nTu veux que je cherche autre chose ? Je suis là ! 😄"

    return response


def is_greeting(user_input: str) -> bool:
    # Liste de salutations avec des variantes
    greetings = [
        "salut", "bonjour", "coucou", "ça va", "yo", "hello", "hey", 
        "boujour", "saluttt", "bonjooor", "salu", "bounjour", "heyyy", "hola","salam"
    ]
    
    # Mise en minuscule et suppression des espaces excédentaires
    user_input_cleaned = user_input.lower().strip()

    # Vérifier si une salutation est présente dans la phrase
    return any(re.search(r'\b' + greet + r'\b', user_input_cleaned) for greet in greetings)

def get_welcome_message(user_name: str = "") -> str:
    greeting = f"Salut {user_name} 👋" if user_name else "Salut 👋"

    message = (
        f"{greeting} ! Je suis **RenalIA**, ton assistant intelligent 📊💬\n"
        "Je vais bien, merci de demander 😄 Et toi, comment vas-tu ?\n\n"
        "Tu peux me poser une question comme :\n"
        "🔍 *« Trouve-moi un logement pas cher sur Paris »*\n"
        "📍 *« Je cherche quelque chose dans le Marais »*\n"
        "je peux effectuer des recherches sur internet si je ne trouve pas de résultats dans mes données ! 🌐\n"
        "Je suis là pour t’aider à trouver ce qu’il te faut en quelques secondes ! 🚀"
    )

    return message

