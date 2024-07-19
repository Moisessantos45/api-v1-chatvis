import nltk

nltk.download("stopwords")

nltk.download("punkt")

import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def process_messages(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    messages = [item["mensaje"] for item in data]

    stop_words = set(stopwords.words("spanish"))
    stemmer = PorterStemmer()
    unique_words = set()

    for message in messages:
        tokens = word_tokenize(message.lower())
        filtered_tokens = [
            stemmer.stem(token)
            for token in tokens
            if token not in stop_words and len(token) > 3
        ]
        unique_words.update(filtered_tokens)

    limited_words = list(unique_words)[:130]

    return limited_words
