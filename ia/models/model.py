import torch.nn as nn # type: ignore

class ChatBotModel(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size):
        super(ChatBotModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.encoder = nn.GRU(embed_size, hidden_size, batch_first=True)
        self.decoder = nn.GRU(embed_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x, hidden=None):
        embedded = self.embedding(x)
        output, hidden = self.encoder(embedded, hidden)
        output, hidden = self.decoder(embedded, hidden)
        logits = self.fc(output)
        return logits