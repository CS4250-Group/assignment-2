def compute_pagerank(links, d=0.85, max_iter=100):
    pages = list(links.keys())
    N = len(pages)
    pr = {page: 1.0 / N for page in pages}

    for _ in range(max_iter):
        new_pr = {}
        for page in pages:
            new_pr[page] = (1 - d) / N
            new_pr[page] += d * sum(
                pr.get(incoming, 0) / len(links[incoming]) 
                for incoming in links if page in links[incoming]
            )
        pr = new_pr
    return pr
