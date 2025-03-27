import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from sentence_transformers import SentenceTransformer 
import pickle
from utils.data_loader import dataframe

model_name = "all-MiniLM-L6-v2"
model = SentenceTransformer(model_name)

# Construire une phrase pour chaque logement
def build_textual_representation(row):
    return f"{row['name']} à {row['neighbourhood']} - Type: {row['room_type']} - Prix: {row['price']}"

# Nettoyage + échantillonnage (si dataset trop gros)
df = dataframe.copy()
df = df.dropna(subset=['name', 'neighbourhood', 'room_type', 'price'])
df = df.sample(10000, random_state=42)  

texts = df.apply(build_textual_representation, axis=1).tolist()

print(" Génération des embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

# Sauvegarde des embeddings
os.makedirs("ai/embeddings", exist_ok=True)

with open("ai/embeddings/embeddings.pkl", "wb") as f:
    pickle.dump({
        "texts": texts,
        "vectors": embeddings,
        "original_rows": df.to_dict(orient="records")
    }, f)

print(f"✅ {len(embeddings)} embeddings sauvegardés dans ai/embeddings/embeddings.pkl")
