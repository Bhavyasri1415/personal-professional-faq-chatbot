import nltk
from nltk.tokenize import word_tokenize


def download_nltk_data():
    """
    Download the NLTK resources required by the chatbot.
    """

    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)


def preprocess_text(text):
    """
    Basic text preprocessing.

    Steps:
    1. Convert text to lowercase.
    2. Remove unnecessary spaces.
    3. Tokenize the sentence.
    4. Join the tokens back into a processed string.
    """

    text = text.lower().strip()

    tokens = word_tokenize(text)

    return " ".join(tokens)