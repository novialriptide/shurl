from typing import Any, Optional

from utils import parse_training_data_from_bson, delete_attributes
from config import CACHE_DIRECTORY
import os
import json
import numpy
import evaluate
import requests

from datasets import load_dataset
from transformers import AutoTokenizer, LongT5ForConditionalGeneration, TrainingArguments, Trainer


class Shurl:
    def __init__(self) -> None:
        self.load_data()
        self.dataset = load_dataset("json", data_files=".shurl-cache/data.json")

        # TODO: Use [LongT5](https://huggingface.co/docs/transformers/en/model_doc/longt5)
        # instead since there is a character limit.
        self.tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
        self.model = LongT5ForConditionalGeneration.from_pretrained("google/long-t5-local-base")
        self.training_args = TrainingArguments(output_dir=".shurl-cache")
        self.trainer: Optional[Trainer] = None

        # self.train()

    def load_data(self) -> Any:
        """Load the training data, this is assuming you're using Shrunk's production database dump."""
        cache_file_path = os.path.join(CACHE_DIRECTORY, "data.json")

        if os.path.isfile(cache_file_path):
            return

        data = parse_training_data_from_bson("data/urls.bson")

        if not os.path.exists(CACHE_DIRECTORY):
            os.makedirs(CACHE_DIRECTORY)

        with open(cache_file_path, "w+") as file:
            json.dump(data, file, indent=4)

        return data

    def train(self) -> None:
        """Train a model using the loaded data."""

        def tokenize_function(examples: Any) -> Any:
            return self.tokenizer(examples["title"], padding="max_length", truncation=True)

        tokenized_datasets = self.dataset.map(tokenize_function, batched=True)
        small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
        metric = evaluate.load("accuracy")

        def compute_metrics(eval_pred: Any) -> Any:
            logits, labels = eval_pred
            predictions = numpy.argmax(logits, axis=-1)
            return metric.compute(predictions=predictions, references=labels)

        self.trainer = Trainer(
            model=self.model,
            args=self.training_args,
            compute_metrics=compute_metrics,
            train_dataset=small_train_dataset,
        )
        self.trainer.train()

    def handle_url(self, url: str) -> str:
        """Feed a URL to Shurl."""
        webpage_contents = requests.get(url).text

        input_ids = self.tokenizer(delete_attributes(webpage_contents), return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        return str(self.tokenizer.decode(outputs[0], skip_special_tokens=True))
