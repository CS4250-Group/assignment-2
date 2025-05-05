from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class VectorSearch:
    def __init__(self, pages):
        self.urls = list(pages.keys())
        self.docs = list(pages.values())
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.docs)

    def search(self, query):
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        ranked = sorted(zip(self.urls, scores), key=lambda x: -x[1])
        return ranked
