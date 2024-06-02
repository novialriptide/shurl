from utils import parse_training_data_from_bson

from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import itertools


class App:
    def __init__(self) -> None:
        self.tfidf = TfidfVectorizer()
        nltk.download("punkt")
        nltk.download("stopwords")
        data = parse_training_data_from_bson("data/urls.bson")
        print(len(data))

    def run(self, text: str, options_count: int = 5) -> List[str]:
        # text = preprocess(text)
        text = text.lower()

        stop_words = set(stopwords.words("english"))
        words = word_tokenize(text)
        filtered_words = [
            word for word in words if word.isalnum() and word not in stop_words
        ]

        common_words = Counter(filtered_words).most_common(15)
        keywords = [word for word, _ in common_words]

        options = []
        for length in range(1, min(5, len(keywords)) + 1):
            for combination in itertools.combinations(keywords, length):
                option = "-".join(combination)
                options.append(option)

        return options[:options_count]


if __name__ == "__main__":
    app = App()
    app.run(
        """The upcoming fields are pretty standard SSH
information , nothing specific for MongoDB."""
    )
