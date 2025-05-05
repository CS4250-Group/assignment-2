import requests
from bs4 import BeautifulSoup

def crawl(seed_url, limit=500):
    visited = set()
    pages = {}
    links = {}

    queue = [seed_url]
    while queue and len(visited) < limit:
        url = queue.pop(0)
        if url in visited or not url.startswith("http"):
            continue

        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            pages[url] = text
            visited.add(url)

            hrefs = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')]
            links[url] = hrefs

            for link in hrefs:
                if link not in visited:
                    queue.append(link)

        except Exception:
            continue

    return pages, links
