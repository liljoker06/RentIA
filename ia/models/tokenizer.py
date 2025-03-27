# tokenizer.py

def tokenize(text):
    return text.lower().split()

def build_vocab(pairs, min_freq=1):
    from collections import Counter
    counter = Counter()
    for q, a in pairs:
        counter.update(tokenize(q))
        counter.update(tokenize(a))

    vocab = {"<PAD>": 0, "<UNK>": 1}
    for word, freq in counter.items():
        if freq >= min_freq:
            vocab[word] = len(vocab)

    idx2word = {i: w for w, i in vocab.items()}
    return vocab, idx2word

def encode_sentence(text, vocab):
    return [vocab.get(token, vocab["<UNK>"]) for token in tokenize(text)]

def pad_sequence(seq, max_len):
    return seq[:max_len] + [0] * max(0, max_len - len(seq))
