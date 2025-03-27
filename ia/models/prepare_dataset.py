import gzip
import json
import sys
import os
from langdetect import detect

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

input_path = "data/oasst/2023-04-12_oasst_ready.trees.jsonl.gz"
base_output_path = "datasets/oasst_dataset"

output_path = f"{base_output_path}.txt"
pairs = set()

def is_french(text):
    try:
        return detect(text) == "fr"
    except:
        return False

def extract_pairs(node):
    if node["role"] != "prompter":
        return
    for reply in node.get("replies", []):
        if reply["role"] == "assistant":
            q = node["text"].strip().replace("\n", " ")
            a = reply["text"].strip().replace("\n", " ")
            
            # 🌍 Vérifie que question ET réponse sont en français
            if is_french(q) and is_french(a):
                pairs.add((q, a))
            
            # 🔁 Extraction récursive
            for sub_reply in reply.get("replies", []):
                extract_pairs(sub_reply)

# 📦 Lecture du fichier gzip
with gzip.open(input_path, "rt", encoding="utf-8") as f:
    for line in f:
        tree = json.loads(line)
        root = tree["prompt"]
        extract_pairs(root)

print(f"✅ {len(pairs)} paires Q/R FR extraites")

# 💾 Sauvegarde
with open(output_path, "w", encoding="utf-8") as f:
    for q, a in pairs:
        f.write(q + "\n")
        f.write(a + "\n")

print(f"💾 Données sauvegardées dans {output_path}")
