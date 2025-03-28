############## test avec RNN ################

import torch.nn as nn

class ChatBotModel(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size):
        super(ChatBotModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)

        # 💡 RNN simple (compatible DirectML)
        self.encoder = nn.RNN(embed_size, hidden_size, batch_first=True)
        self.decoder = nn.RNN(embed_size, hidden_size, batch_first=True)

        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x, hidden=None):
        embedded = self.embedding(x)
        output, hidden = self.encoder(embedded, hidden)
        output, hidden = self.decoder(embedded, hidden)
        logits = self.fc(output)
        return logits


############## test avec GRU ################

# import torch.nn as nn 

# class ChatBotModel(nn.Module):
#     def __init__(self, vocab_size, embed_size, hidden_size):
#         super(ChatBotModel, self).__init__()
#         self.embedding = nn.Embedding(vocab_size, embed_size)
#         self.encoder = nn.GRU(embed_size, hidden_size, batch_first=True)
#         self.decoder = nn.GRU(embed_size, hidden_size, batch_first=True)
#         self.fc = nn.Linear(hidden_size, vocab_size)

#     def forward(self, x, hidden=None):
#         embedded = self.embedding(x)
#         output, hidden = self.encoder(embedded, hidden)
#         output, hidden = self.decoder(embedded, hidden)
#         logits = self.fc(output)
#         return logits


############## test avec LSTM###########

# import torch.nn as nn

# class ChatBotModel(nn.Module):
#     def __init__(self, vocab_size, embed_size, hidden_size):
#         super(ChatBotModel, self).__init__()
#         self.embedding = nn.Embedding(vocab_size, embed_size)
        
#         # 🔁 LSTM au lieu de GRU
#         self.encoder = nn.LSTM(embed_size, hidden_size, batch_first=True)
#         self.decoder = nn.LSTM(embed_size, hidden_size, batch_first=True)

#         self.fc = nn.Linear(hidden_size, vocab_size)

#     def forward(self, x, hidden=None):
#         embedded = self.embedding(x)

#         # ✨ LSTM retourne (output, (hidden, cell))
#         output, (hidden, cell) = self.encoder(embedded)
#         output, (hidden, cell) = self.decoder(embedded, (hidden, cell))

#         logits = self.fc(output)
#         return logits
