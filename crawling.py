from collections import defaultdict
from indexing import *
from bs4 import BeautifulSoup
import requests
import os

def crawl(seed_url, max_pages):
    # Initialize a set to store visited URLs
    visited_urls = set()

    # Initialize a list to store URLs to be crawled
    url_queue = [seed_url]

    # Initialize an inverted index
    inverted_index = defaultdict(list)

    # Start crawling
    while url_queue and len(visited_urls) < max_pages:
        # Get the next URL from the queue
        url = url_queue.pop(0)

        # Fetch the web page
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            continue

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information from the page
        # In this example, we're saving the page content to a file
        page_content = response.text
        save_page_content(url, page_content)

        # Index the page content
        index_page_content(url, page_content, inverted_index)

        # Add the URL to the set of visited URLs
        visited_urls.add(url)

        # Save the URL to the output file
        save_url(url)

        # Find all links on the page and add them to the queue
        for link in soup.find_all('a'):
            href = link.get('href')

            # Handle relative URLs
            if href and not href.startswith('http'):
                href = url + href

            # Add the URL to the queue if it hasn't been visited yet
            if href not in visited_urls and href not in url_queue:
                url_queue.append(href)

    # Save the inverted index to a file
    save_inverted_index(inverted_index)
    return inverted_index  # Return inverted_index data structure

def save_page_content(url, content):
    # Generate a file name based on the URL
    file_name = url.replace('/', '_').replace(':', '') + '.html'
    file_path = os.path.join('pages', file_name)

    # Save the content to a file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def save_url(url):
    # Append the URL to the output file
    with open('output.txt', 'a', encoding='utf-8') as file:
        file.write(url + '\n')

