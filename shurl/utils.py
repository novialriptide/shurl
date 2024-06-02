from typing import List, Any
from bs4 import BeautifulSoup
import requests
import bson
import urllib3
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


def parse_useful_elements(html_content: str) -> List[str]:
    valid_elements = ["li", "p", "span", "h1", "h2", "h3", "h4", "h5", "h6"]
    out = []

    page = BeautifulSoup(html_content, "html.parser")
    for element in valid_elements:
        for p in page.find_all(element):
            out.append(p.text.strip())

    return out


def parse_training_data_from_bson(file_path: str) -> List[dict[str, Any]]:
    """
    Parse training data from a BSON file, this will
    be cached in `.shurl-cache`.

    BSON is a filetype made by MongoDB.

    @file_path: The path of the BSON file from Shrunk.
    """

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    with open(file_path, "rb") as file:
        urls_data = bson.decode_all(file.read())

    parsed_data = []

    for url in urls_data:
        if len(url["aliases"]) == 0:
            continue

        alias = url["aliases"][0]["alias"]
        if "-" not in alias:
            continue

        try:
            webpage_response = requests.get(
                url["long_url"],
                timeout=5,
                verify=False,
            )
            if webpage_response.status_code != 200:
                continue

            webpage_contents = parse_useful_elements(webpage_response.text)
        except requests.exceptions.Timeout:
            continue

        document = {
            "original_url": url["long_url"],
            "aliases": [alias["alias"] for alias in url["aliases"]],
            "webpage_contents": webpage_contents,
        }

        parsed_data.append(document)

    return parsed_data
