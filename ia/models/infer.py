import torch
import torch.nn.functional as F
import torch_directml
import os
import pickle
from model import ChatBotModel
from tokenizer import encode_sentence, pad_sequence
from collections import Counter

# 📦 Paramètres
EMBED_SIZE = 128
HIDDEN_SIZE = 256
MAX_LEN = 20

USE_CPU_ONLY = True
DEVICE = "cpu" if USE_CPU_ONLY else torch_directml.device()
# DEVICE = torch_directml.device()

print(f"📟 GPU utilisé : {DEVICE}")

# 📁 Chargement auto des modèles + vocabs
model_dir = "trained"
models = []

for file in os.listdir(model_dir):
    if file.startswith("chatbot_model") and file.endswith(".pth"):
        version = file.replace("chatbot_model_", "").replace(".pth", "")
        model_path = os.path.join(model_dir, file)
        vocab_path = os.path.join(model_dir, f"vocab_{version}.pkl")
        if os.path.exists(vocab_path):
            models.append((version, model_path, vocab_path))

if not models:
    print("❌ Aucun modèle trouvé dans /model/")
    exit()

# 🧠 Chargement des modèles
loaded_models = []
for version, model_path, vocab_path in models:
    with open(vocab_path, "rb") as f:
        word2idx, idx2word = pickle.load(f)
    vocab_size = len(word2idx)

    model = ChatBotModel(vocab_size, EMBED_SIZE, HIDDEN_SIZE).to(DEVICE)
    # model.load_state_dict(torch.load(model_path, map_location=DEVICE))
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.to(DEVICE)
    model.eval()

    loaded_models.append({
        "name": version,
        "model": model,
        "word2idx": word2idx,
        "idx2word": idx2word
    })

# ✨ Récupérer une réponse par modèle
def get_response(text, m):
    word2idx = m["word2idx"]
    idx2word = m["idx2word"]
    model = m["model"]

    encoded = encode_sentence(text, word2idx)
    padded = pad_sequence(encoded, MAX_LEN)
    input_tensor = torch.tensor([padded]).to(DEVICE)

    with torch.no_grad():
        output = model(input_tensor)[0]
    predicted_ids = torch.argmax(F.softmax(output, dim=-1), dim=-1).tolist()
    tokens = [idx2word.get(idx, "") for idx in predicted_ids]
    filtered = [t for t in tokens if t not in ["<PAD>", "<UNK>", ""]]
    return " ".join(filtered).strip()

# 📊 Choisir la réponse la plus fréquente
def select_best_response(responses):
    return Counter(responses).most_common(1)[0][0]

# 💬 Interface
if __name__ == "__main__":
    print("🤖 IA Multi-modèles prête ! (tape 'exit' pour quitter)\n")
    while True:
        user_input = input("👤 Toi : ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 À bientôt !")
            break

        responses = [get_response(user_input, m) for m in loaded_models]
        final_response = select_best_response(responses)
        print(f"🤖 IA : {final_response}\n")
