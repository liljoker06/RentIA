import os 
import pickle
import numpy as np 
from sentence_transformers import SentenceTransformer 
from sklearn.metrics.pairwise import cosine_similarity 


# Charger les embeddings

with open("ai/embeddings/embeddings.pkl", "rb") as f:
    data = pickle.load(f)

texts = data["texts"]
vectors = data["vectors"]
original_rows = data["original_rows"]

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_similar_rows(question: str, top_k: int = 5):
    question_embedding = model.encode([question])

    # Calculer les similarités
    similarities = cosine_similarity(question_embedding, vectors)[0]

    # Récupérer les indices des top_k similarités
    top_indices = np.argsort(similarities)[::-1][:top_k]

    #resultat 
    results = []
    for i in top_indices:
        results.append({
            "score": round(similarities[i], 3),
            "text": texts[i],
            "data": original_rows[i]
        })
    return results

# # Test rapide
# if __name__ == "__main__":
#     q = input("Pose une question à l'IA : ")
#     resultats = retrieve_similar_rows(q)

#     for r in resultats:
#         print(f"\n🔹 Score: {r['score']}")
#         print(f"📝 {r['text']}")
#         print(f"📊 Données : {r['data']}")