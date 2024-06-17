import math
from collections import defaultdict

def calculate_tf_idf(inverted_index):
    # Calculate term frequencies (TF) and document frequencies (DF)
    term_frequencies = defaultdict(int)
    document_frequencies = defaultdict(int)
    for term, postings in inverted_index.items():
        # Calculate the term frequency (TF) for each term
        term_frequencies[term] = len(postings)
        for doc in postings:
            # Calculate the document frequency (DF) for each document
            document_frequencies[doc] += 1

    # Calculate inverse document frequencies (IDF)
    num_documents = len(document_frequencies)
    inverse_document_frequencies = {doc: math.log(num_documents / (df + 1)) for doc, df in document_frequencies.items()}

    # Calculate TF-IDF scores
    tf_idf_scores = defaultdict(dict)
    for term, postings in inverted_index.items():
        for doc in postings:
            # Calculate the TF-IDF score for each term-document pair
            tf_idf_scores[term][doc] = term_frequencies[term] * inverse_document_frequencies[doc]

    # Save the TF-IDF scores to a file
    with open('tf_idf_scores.txt', 'w', encoding='utf-8') as file:
        for term, scores in tf_idf_scores.items():
            scores_str = ', '.join([f'{doc}: {score}' for doc, score in scores.items()])
            file.write(f'{term}: {scores_str}\n')

    return tf_idf_scores