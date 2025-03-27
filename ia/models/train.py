import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import os
import torch_directml
import pickle

from tokenizer import build_vocab, encode_sentence, pad_sequence
from model import ChatBotModel

from tqdm import tqdm
import time
start_time = time.time()



USE_CPU_ONLY = True

# 💻 Utiliser le GPU AMD via DirectML
device = "cpu" if USE_CPU_ONLY else torch_directml.device()
print(f"📟 Entraînement sur : {device}")

torch.set_num_threads(os.cpu_count())
print(f"🧠 Nombre de threads utilisés : {torch.get_num_threads()}")

# 🔧 Paramètres
EMBED_SIZE = 128
HIDDEN_SIZE = 256
BATCH_SIZE = 128 # 32
EPOCHS = 10
MAX_LEN = 20
DATASET_DIR = "datasets"

# 📂 Lire tous les fichiers .txt dans le dossier datasets
lines = []
for file in os.listdir(DATASET_DIR):
    if file.endswith(".txt"):
        path = os.path.join(DATASET_DIR, file)
        print(f"📄 Chargement : {file}")
        with open(path, "r", encoding="utf-8") as f:
            lines += f.read().strip().split("\n")

print(f"🔢 Lignes totales : {len(lines)}")

# 🔀 Création des paires (Q/R)
pairs = [(lines[i], lines[i + 1]) for i in range(0, len(lines) - 1, 2)]

# 🧠 Vocabulaire
word2idx, idx2word = build_vocab(pairs)
vocab_size = len(word2idx)

# Dataset PyTorch
class DialogueDataset(Dataset):
    def __init__(self, pairs):
        self.data = pairs

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        q, a = self.data[idx]
        q_ids = pad_sequence(encode_sentence(q, word2idx), MAX_LEN)
        a_ids = pad_sequence(encode_sentence(a, word2idx), MAX_LEN)
        return torch.tensor(q_ids), torch.tensor(a_ids)

dataset = DialogueDataset(pairs)
loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

# 📦 Modèle, loss, optim
model = ChatBotModel(vocab_size, EMBED_SIZE, HIDDEN_SIZE).to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 🚀 Entraînement
for epoch in range(EPOCHS):
    model.train()
    total_loss = 0

    for batch in tqdm(loader, desc=f"🔁 Epoch {epoch+1}/{EPOCHS}", leave=False):
        input_seq, target_seq = [x.to(device) for x in batch]
        optimizer.zero_grad()

        output = model(input_seq)
        output = output.view(-1, vocab_size)
        target_seq = target_seq.view(-1)

        loss = loss_fn(output, target_seq)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    duration = round(time.time() - start_time, 2)
    print(f"🧠 Epoch {epoch+1}/{EPOCHS} - Loss: {total_loss:.4f} - ⏱️ {duration}s")




os.makedirs("trained", exist_ok=True)
def get_next_model_version(base_name="chatbot_model"):
    version = 1
    while True:
        model_path = f"trained/{base_name}_V{version}.pth"
        vocab_path = f"trained/vocab_V{version}.pkl"
        if not os.path.exists(model_path) and not os.path.exists(vocab_path):
            return model_path, vocab_path
        version += 1


model_path, vocab_path = get_next_model_version()

# 💾 Sauvegarde
torch.save(model.state_dict(), model_path)
print(f"✅ Modèle sauvegardé : {model_path}")

with open(vocab_path, "wb") as f:
    pickle.dump((word2idx, idx2word), f)
print(f"📚 Vocabulaire sauvegardé : {vocab_path}")
