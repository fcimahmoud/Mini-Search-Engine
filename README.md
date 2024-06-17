# This implementation demonstrates a basic web crawler and search engine

## 1. **crawling**:
   - The `crawl` function takes a seed URL and a maximum number of pages to crawl.
   - It initializes a set to track visited URLs and a list to store URLs to be crawled.
   - It also initializes an inverted index, which maps terms to the URLs where they appear.
   - The function fetches web pages, extracts relevant information (in this case, the page content), saves the content to files, and indexes the content.
   - Finally, it saves the inverted index to a file.

## 2. **indexing**:
   - The `index_page_content` function takes a URL, the page content, and an inverted index as input.
   - It tokenizes the content, removes stop words, stems the tokens, and normalizes them.
   - It then updates the inverted index, mapping each term to the URLs where it appears.
   - The `save_inverted_index` function writes the inverted index to a file.

## 3. **tf_idf**:
   - The `calculate_tf_idf` function calculates the term frequency (TF) and document frequency (DF) for each term in the inverted index.
   - It then calculates the inverse document frequency (IDF) for each document.
   - Finally, it computes the TF-IDF scores for each term-document pair and saves them to a file.

## 4. **search**:
   - The `perform_search` function takes a query, the inverted index, and the TF-IDF scores as input.
   - It tokenizes the query, removes stop words, stems the tokens, and normalizes them.
   - It then calculates the relevance scores for each document based on the TF-IDF scores and the query terms.
   - The function returns a list of documents sorted by their relevance scores.
   - The `save_search_results` function writes the search results to a file.

## 5. **main**:
   - The `main` function is the entry point of the application.
   - It calls the `crawl` function to build the inverted index and calculate the TF-IDF scores.
   - It then enters a loop, where the user can enter a search query. The search results are written to a file.
