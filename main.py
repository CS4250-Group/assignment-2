from crawler import crawl
from indexer import build_inverted_index, save_index
from boolean_search import boolean_retrieval
from vector_search import VectorSearch
from pagerank import compute_pagerank
from combined_search import combined_search

def main():
    seed_url = "https://www.bbc.com/news"
    
    print("[1] Crawling pages...")
    pages, links = crawl(seed_url)

    print("[2] Building inverted index...")
    inverted_index = build_inverted_index(pages)

    print("[3] Setting up vector search...")
    vector_model = VectorSearch(pages)

    print("[4] Computing PageRank...")
    pagerank_scores = compute_pagerank(links)

    query = input("Enter search query: ")

    print("\n--- Boolean Retrieval ---")
    boolean_results = boolean_retrieval(query, inverted_index)
    for url in boolean_results:
        print(url)

    print("\n--- Combined Vector + PageRank ---")
    combined_results = combined_search(query, vector_model, pagerank_scores)
    for url, score in combined_results[:10]:
        print(f"{url} (score: {score:.4f})")

if __name__ == "__main__":
    main()
