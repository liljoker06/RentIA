from duckduckgo_search import DDGS 

def search_web(query: str, max_results: int = 3) -> list:
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, region='fr-fr', safesearch='Moderate', max_results=max_results):
            results.append({
                "title": r.get("title"),
                "href": r.get("href"),
                "snippet": r.get("body")
            })
    return results
