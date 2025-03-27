import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import os
import torch_directml
import pickle
from datasets import load_dataset
from tokenizer import build_vocab, encode_sentence, pad_sequence
from model import ChatBotModel
from tqdm import tqdm
import time

start_time = time.time()

USE_CPU_ONLY = False  # Changer à False pour utiliser le GPU via DirectML

# 💻 Utiliser le GPU AMD via DirectML
device = "cpu" if USE_CPU_ONLY else torch_directml.device()
print(f"📟 Entraînement sur : {device}")

torch.set_num_threads(os.cpu_count())
print(f"🧠 Nombre de threads utilisés : {torch.get_num_threads()}")

# 🔧 Paramètres
EMBED_SIZE = 128
HIDDEN_SIZE = 256
BATCH_SIZE = 32  # 128 pour plus rapide, mais peut être ajusté
EPOCHS = 10
MAX_LEN = 20
BATCH_SIZE_LINES = 50000  # Nombre de lignes par tranche

# 📂 Charger le dataset Claire-Dialogue (en streaming)
dataset = load_dataset("oscar", "unshuffled_deduplicated_fr", streaming=True)

print("📚 Dataset chargé")

# Fonction pour diviser en tranches de données
def get_batches(dataset, batch_size_lines):
    lines = []
    for dialogue in dataset['train']:  # Assurez-vous que 'train' est la bonne partition
        q = dialogue['text'].strip()
        a = q  # Utilisation du même texte comme réponse pour simplification
        lines.append((q, a))

        # Quand on a atteint le nombre de lignes par tranche, renvoie les données
        if len(lines) == batch_size_lines:
            yield lines
            lines = []  # Réinitialiser la liste pour la prochaine tranche

    # Traiter le reste s'il en reste
    if lines:
        yield lines

# Ajouter la fonction get_next_model_version
def get_next_model_version(base_name="chatbot_model"):
    version = 1
    while True:
        model_path = f"trained/{base_name}_V{version}.pth"
        vocab_path = f"trained/vocab_V{version}.pkl"
        if not os.path.exists(model_path) and not os.path.exists(vocab_path):
            return model_path, vocab_path
        version += 1

# 🧠 Vocabulaire
print("🔠 Construction du vocabulaire...")
pairs = []
for batch in get_batches(dataset, BATCH_SIZE_LINES):
    pairs.extend(batch)

word2idx, idx2word = build_vocab(pairs)
vocab_size = len(word2idx)

print(f"📚 Vocabulaire construit - Taille : {vocab_size}")

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

# 📦 Modèle, loss, optim
model = ChatBotModel(vocab_size, EMBED_SIZE, HIDDEN_SIZE).to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 🚀 Entraînement avec batch et sauvegarde après chaque tranche
for epoch in range(EPOCHS):
    model.train()
    total_loss = 0

    # Affichage de la barre de progression pour chaque tranche
    for batch_idx, batch in tqdm(enumerate(get_batches(dataset, BATCH_SIZE_LINES)), desc=f"🔁 Epoch {epoch+1}/{EPOCHS}", leave=False):
        input_seq, target_seq = [x.to(device) for x in batch]
        optimizer.zero_grad()

        output = model(input_seq)
        output = output.view(-1, vocab_size)
        target_seq = target_seq.view(-1)

        loss = loss_fn(output, target_seq)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

        # Sauvegarde après chaque batch
        model_path, vocab_path = get_next_model_version(base_name="chatbot_model")
        torch.save(model.state_dict(), model_path)
        with open(vocab_path, "wb") as f:
            pickle.dump((word2idx, idx2word), f)

    duration = round(time.time() - start_time, 2)
    print(f"🧠 Epoch {epoch+1}/{EPOCHS} - Loss: {total_loss:.4f} - ⏱️ {duration}s")
    print(f"✅ Modèle sauvegardé après le batch : {model_path}")
    print(f"📚 Vocabulaire sauvegardé après le batch : {vocab_path}")
    

# 💾 Sauvegarde du modèle final
print("💾 Enregistrement du modèle final...")
model_path, vocab_path = get_next_model_version(base_name="chatbot_model_final")
torch.save(model.state_dict(), model_path)
with open(vocab_path, "wb") as f:
    pickle.dump((word2idx, idx2word), f)
print(f"✅ Modèle final sauvegardé : {model_path}")
print(f"📚 Vocabulaire final sauvegardé : {vocab_path}")
