from typing import List, Dict

def generate_response(results: List[Dict], user_question: str = "") -> str:
    if not results:
        return "Hmm... j’ai fouillé dans les données, mais je n’ai rien trouvé qui corresponde vraiment à ta question 😕."

    top_result = results[0]
    logement = top_result['data']
    score = top_result['score']

    name = logement.get("name", "un logement sans nom")
    quartier = logement.get("neighbourhood", "un quartier inconnu")
    room_type = logement.get("room_type", "un type inconnu")
    prix = logement.get("price", "un prix inconnu")

    # Moyenne des prix
    prices = [row["data"].get("price", 0) for row in results if isinstance(row["data"].get("price", 0), (int, float))]
    avg_price = round(sum(prices) / len(prices), 2) if prices else "?"

    # 🔥 Réponse naturelle avec la question incluse
    response = f"🔍 En réponse à ta question : « {user_question} », voici ce que j’ai trouvé 👇\n\n"
    response += f"🏠 *{name}* est un logement situé à **{quartier}**.\n"
    response += f"C’est un type de logement : **{room_type}**, proposé à environ **{prix} €**.\n"
    response += f"\n📊 Le prix moyen des logements similaires est de **{avg_price} €**.\n"
    response += f"\n🤖 (Indice de pertinence : {round(score * 100)}%)\n"
    response += f"\nTu veux que je cherche autre chose ? Je suis là ! 😄"

    return response
