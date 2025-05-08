from crawler import crawl
from indexer import build_inverted_index, save_index
from boolean_search import boolean_retrieval
from vector_search import VectorSearch
from pagerank import compute_pagerank
from combined_search import combined_search
import csv

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

    # loop and print each result from boolean retrieval
    print("\n--- Boolean Retrieval ---")
    boolean_results = boolean_retrieval(query, inverted_index)
    for url in boolean_results:
        print(url)

    # loop and print the top 10 combined search results with scores 
    print("\n--- Combined Vector + PageRank ---")
    combined_results = combined_search(query, vector_model, pagerank_scores)
    for url, score in combined_results[:10]:
        print(f"{url} (score: {score:.4f})")

    # get top 100 pages by PageRank
    top_100 = sorted(pagerank_scores.items(), key=lambda x: -x[1])[:100]

    # print top 100 to console
    print("\n--- Top 100 Pages by PageRank ---")
    for url, score in top_100:
        print(f"{url} (PageRank: {score:.6f})")

    # save top 100 to csv
    with open("top_100_pagerank.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Rank", "URL", "PageRank Score"])
        for i, (url, score) in enumerate(top_100, 1):
            writer.writerow([i, url, round(score, 6)])

if __name__ == "__main__":
    main()
