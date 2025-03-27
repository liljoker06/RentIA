import gzip
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from langdetect import detect

input_path = "data/oasst/2023-04-12_oasst_ready.trees.jsonl.gz"
base_output_path = "datasets/oasst_dataset"

# 🔁 Générer le nom de fichier avec version auto
def get_available_filename(base_path):
    version = 1
    while True:
        full_path = f"{base_path}_V{version}.txt"
        if not os.path.exists(full_path):
            return full_path
        version += 1

output_path = get_available_filename(base_output_path)
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
            # 🔒 Anti-doublons
            pairs.add((q, a))
            # Extraction récursive
            for sub_reply in reply.get("replies", []):
                extract_pairs(sub_reply)

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
