from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# vectorizer & tf-idf matrix
class VectorSearch:
    def __init__(self, pages):
        self.urls = list(pages.keys())
        self.docs = list(pages.values())
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.docs)

    # compute similarity scores for queries
    def search(self, query):
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        # sorted by descending similarity scores
        ranked = sorted(zip(self.urls, scores), key=lambda x: -x[1])
        return ranked
