# finds documents that contains all the words in the query using an inverted index

def boolean_retrieval(query, inverted_index):
    words = query.lower().split()
    if not words:
        return set()
    
    result = inverted_index.get(words[0], set())
    for word in words[1:]:
        result &= inverted_index.get(word, set())
    return result
