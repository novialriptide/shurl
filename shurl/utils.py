from typing import List
import re


def preprocess(value: str) -> List[str]:
    """
    Preprocess the text and returns a list of tokens before it can be fed to
    the deep-learning model.
    """

    value = value.lower()

    # Removes any text with square brackets, parentheses, and punctuation
    value = re.sub(r"\([^)]*\)|\[[^]]*\]|\.|!|\?|,", "", value)

    return value.split()
