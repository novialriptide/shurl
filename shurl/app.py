from utils import parse_training_data_from_bson
from config import CACHE_DIRECTORY
from typing import List
import os
import json


class App:
    def __init__(self) -> None:
        self.execute_cache()

    def execute_cache(self) -> None:
        cache_file_path = os.path.join(CACHE_DIRECTORY, "data.json")

        if os.path.isfile(cache_file_path):
            return

        data = parse_training_data_from_bson("data/urls.bson")

        if not os.path.exists(CACHE_DIRECTORY):
            os.makedirs(CACHE_DIRECTORY)

        with open(cache_file_path, "w+") as file:
            json.dump(data, file, indent=4)

    def run(self, text: str, options_count: int = 5) -> List[str]:
        return []


if __name__ == "__main__":
    app = App()
    app.run(
        """The upcoming fields are pretty standard SSH
information , nothing specific for MongoDB."""
    )
