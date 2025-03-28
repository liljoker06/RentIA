from googlesearch import search
from typing import List, Dict

def search_web(query: str, count: int = 5) -> List[Dict]:
    """
    Effectue une recherche sur le web en utilisant Google.

    Args:
        query (str): La requête de recherche.
        count (int): Nombre de résultats à retourner.

    Returns:
        List[Dict]: Liste des résultats de recherche avec titre et lien.
    """
    results = []
    for url in search(query, num_results=count):
        results.append({
            "title": url,
            "href": url
        })
    return results
