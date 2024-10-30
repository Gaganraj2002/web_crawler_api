import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from loguru import logger


def crawl_website(url, depth):
    visited_urls = set()
    to_visit = [(url, 0)]
    crawled_links = []

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
    )

    while to_visit:
        current_url, current_depth = to_visit.pop(0)

        if current_depth > depth:
            continue

        if current_url in visited_urls:
            continue

        visited_urls.add(current_url)
        crawled_links.append(current_url)

        try:
            response = session.get(current_url)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to crawl {current_url}: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a", href=True):
            absolute_url = urljoin(current_url, link["href"])
            if urlparse(absolute_url).netloc == urlparse(url).netloc:
                to_visit.append((absolute_url, current_depth + 1))

        logger.info(f"Crawled: {current_url}")
        logger.info(f"Depth: {current_depth}")
        logger.info(f"Total links: {len(crawled_links)}")
        logger.info("----------------------------------")

    return crawled_links
