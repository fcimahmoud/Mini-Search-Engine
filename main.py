from crawling import *
from indexing import *
from tf_idf import *
from search import *

def main():
    # Crawl the web and retrieve inverted index and TF-IDF scores
    seed_url = "https://www.bbc.com"  # Replace with your starting URL
    max_pages = 1000
    inverted_index = crawl(seed_url, max_pages)
    tf_idf_scores = calculate_tf_idf(inverted_index)

    # Enter a search query
    while True:
        query = input("Enter your search query (or 'q' to quit): ")
        if query.lower() == 'q':
            break

        # Perform the search
        sorted_documents = perform_search(query, inverted_index, tf_idf_scores)

        # Write search results to file
        save_search_results(sorted_documents)
        print("Search results written to search_results.txt.")

if __name__ == '__main__':
    main()