from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import math
from collections import defaultdict

def perform_search(query, inverted_index, tf_idf_scores):
    # Tokenize the query
    tokens = word_tokenize(query)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words and token.isalnum()]

    # Stem the tokens
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token.lower()) for token in filtered_tokens]

    # Normalize the tokens
    normalized_tokens = [re.sub(r'\W+', '', token) for token in stemmed_tokens]

    # Initialize a dictionary to store relevance scores
    relevance_scores = defaultdict(float)

    # Calculate relevance scores
    for term in normalized_tokens:
        if term in inverted_index:
            postings = inverted_index[term]
            idf = math.log(len(tf_idf_scores) / len(postings))
            for doc in postings:
                relevance_scores[doc] += tf_idf_scores[term][doc] * idf

    # Sort the documents based on their relevance scores
    sorted_documents = sorted(relevance_scores, key=lambda x: relevance_scores[x], reverse=True)

    return sorted_documents


def save_search_results(sorted_documents):
    # Write search results to file
    with open("search_results.txt", "w") as file:
        if sorted_documents:
            file.write("Search results:\n")
            for doc in sorted_documents:
                file.write(f"- Document: {doc}\n")
        else:
            file.write("No documents found for your query.\n")