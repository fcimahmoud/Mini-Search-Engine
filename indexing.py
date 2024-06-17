from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

def index_page_content(url, content, inverted_index):
    # This function splits a text string into a list of words (tokens).
    tokens = word_tokenize(content)

    # This function provides access to a list of common stop words (e.g., "the," "a," "is").
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words and token.isalnum()]

    # This function can be used to stem words (reduce them to their base form).
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token.lower()) for token in filtered_tokens]

    # It removes non-word characters (punctuation, symbols) using regular expressions.
    normalized_tokens = [re.sub(r'\W+', '', token) for token in stemmed_tokens]

    # This creates a mapping between terms and the webpages where they appear.
    for token in normalized_tokens:
        inverted_index[token].append(url)


def save_inverted_index(inverted_index):
    # Save the inverted index to a file
    with open('inverted_index.txt', 'w', encoding='utf-8') as file:
        for term, postings in inverted_index.items():
            postings_str = ' '.join(postings)
            file.write(f'{term}: {postings_str}\n')