from utils.web_search import search_web
from ai.retriever import retrieve_similar_rows
from ai.responder import generate_response

def process_user_message(message: str) -> str:
    results = retrieve_similar_rows(message)

    if results:
        return generate_response(results, user_question=message)

    # 🌐 Recherche internet si rien trouvé
    web_results = search_web(message)
    if not web_results:
        return "Désolé, je n’ai rien trouvé dans mes données ni sur Internet 😔"

    # 🔁 Sinon on construit une réponse simple avec les résultats web
    response = f"Je n’ai rien trouvé dans mes données, mais voici ce que j’ai trouvé sur le web 🌍 :\n"
    for i, r in enumerate(web_results):
        response += f"\n🔹 {r['title']}\n{r['snippet']}\n🔗 {r['href']}\n"
    return response
