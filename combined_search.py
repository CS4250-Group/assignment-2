# combine the vector search scores and pagerank scores

def combined_search(query, vector_model, pagerank_scores, alpha=0.5):
    results = vector_model.search(query)
    combined = []
    for url, score in results:
        pr = pagerank_scores.get(url, 0)
        combined_score = alpha * score + (1 - alpha) * pr
        combined.append((url, combined_score))

        # sorted in descending order of combined score
    return sorted(combined, key=lambda x: -x[1])
