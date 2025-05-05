import re
from collections import defaultdict
import pickle

def build_inverted_index(pages):
    index = defaultdict(set)
    for url, text in pages.items():
        words = re.findall(r'\w+', text.lower())
        for word in words:
            index[word].add(url)
    return index

def save_index(index, filename="data/index.pkl"):
    with open(filename, 'wb') as f:
        pickle.dump(index, f)

def load_index(filename="data/index.pkl"):
    with open(filename, 'rb') as f:
        return pickle.load(f)
