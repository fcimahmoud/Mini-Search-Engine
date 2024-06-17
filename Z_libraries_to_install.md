Requests: A library for making HTTP requests in Python.
# pip install requests

BeautifulSoup: A library for parsing HTML and XML documents.
# pip install beautifulsoup4

NLTK: The Natural Language Toolkit provides various functionalities for natural language processing, including tokenization, stop word removal, and stemming.
# pip install nltk

If any Errors appeared you could try this:
Upgrade pip to the latest version by running the following command:
# pip install --upgrade pip
Try installing NLTK again:
# pip install nltk

Additionally, you'll need to download the required NLTK data. After installing NLTK, run the following code in Python file for the first time:
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')