from typing import List, Any
from bs4 import BeautifulSoup
import bs4
import requests
import bson
import urllib3
import re
from config import IGNORED_DOMAINS, ONLY_ACCEPT_OK_RESPONSES, REJECT_PDF_CONTENT, REJECT_IMAGE_CONTENT


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

    try:
        page = BeautifulSoup(html_content, "html.parser")
        for element in valid_elements:
            for p in page.find_all(element):
                out.append(p.text.strip())
    except bs4.builder.ParserRejectedMarkup:
        pass

    return out


def delete_attributes(html_content: str) -> str:
    page = BeautifulSoup(html_content, "html.parser")
    for tag in page.find_all():
        if "style" in tag.attrs:
            del tag.attrs["style"]
        if "class" in tag.attrs:
            del tag.attrs["class"]

    return str(page)


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
        for domain in IGNORED_DOMAINS:
            if domain in url["long_url"]:
                continue

        if len(url["aliases"]) == 0:
            continue

        # As of June 5th 2024, Shrunk does not specify if an alias is custom or not.
        # This is a temporary solution.
        met_requirements = False
        for alias in url["aliases"]:
            alias = alias["alias"]
            if "-" in alias or "_" in alias:
                met_requirements = True

        if not met_requirements:
            continue

        try:
            webpage_response = requests.get(
                url["long_url"],
                timeout=5,
                verify=False,
            )
            if webpage_response.status_code != 200 and ONLY_ACCEPT_OK_RESPONSES:
                continue

            if (
                "Content-Type" in webpage_response.headers
                and webpage_response.headers["Content-Type"] == "application/pdf"
                and REJECT_PDF_CONTENT
            ):
                continue

            if (
                "Content-Type" in webpage_response.headers
                and (webpage_response.headers["Content-Type"] in ["image/jpeg", "image/png", "image/gif"])
                and REJECT_IMAGE_CONTENT
            ):
                continue

            webpage_contents = delete_attributes(webpage_response.text)
        except requests.exceptions.Timeout:
            continue
        except requests.exceptions.ConnectionError:
            continue
        except requests.exceptions.TooManyRedirects:
            continue
        except requests.exceptions.RequestException:
            continue

        for alias in url["aliases"]:
            alias = alias["alias"]

            if not ("-" in alias or "_" in alias):
                continue

            document = {
                "title": url["title"],
                "original_url": url["long_url"],
                "aliases": alias,
                "webpage_contents": webpage_contents,
            }

            parsed_data.append(document)
            print(f"Loaded: {alias} {url['long_url']}")

    return parsed_data
