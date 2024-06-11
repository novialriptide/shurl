from typing import Any

from utils import parse_training_data_from_bson, delete_attributes
from config import CACHE_DIRECTORY
import os
import json
import requests

from transformers import T5Tokenizer, T5ForConditionalGeneration


class Shurl:
    def __init__(self, epoch_count: int, batch_size: int) -> None:
        self.load_data()
        self.epoch_count = epoch_count
        self.batch_size = batch_size

        self.tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-small")
        self.model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")

    def load_data(self) -> Any:
        cache_file_path = os.path.join(CACHE_DIRECTORY, "data.json")

        if os.path.isfile(cache_file_path):
            return

        data = parse_training_data_from_bson("data/urls.bson")

        if not os.path.exists(CACHE_DIRECTORY):
            os.makedirs(CACHE_DIRECTORY)

        with open(cache_file_path, "w+") as file:
            json.dump(data, file, indent=4)

        return data

    def handle_url(self, url: str) -> str:
        webpage_contents = requests.get(url).text

        input_ids = self.tokenizer(delete_attributes(webpage_contents), return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        return str(self.tokenizer.decode(outputs[0], skip_special_tokens=True))
