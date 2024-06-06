from typing import Any, Optional
from keras import Model, layers, Input as KeraInput
from positional_embedding import PositionalEmbedding
from decoder import ShurlDecoder
from encoder import ShurlEncoder
from utils import parse_training_data_from_bson
from config import CACHE_DIRECTORY
import os
import json


class Shurl:
    def __init__(self, epoch_count: int, batch_size: int) -> None:
        self.load_data()
        self.epoch_count = epoch_count
        self.batch_size = batch_size

        self.transformer: Optional[Model] = None

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

    def assemble_model(self) -> None:
        """Assemble the end-to-end model."""
        vocab_size = 15000
        sequence_length = 20

        embed_dim = 256
        latent_dim = 2048
        num_heads = 8

        encoder_inputs = KeraInput(shape=(None), dtype="int64", name="encoder_inputs")
        x = PositionalEmbedding(sequence_length, vocab_size, embed_dim)(encoder_inputs)
        encoder_outputs = ShurlEncoder(embed_dim, latent_dim, num_heads)(x)

        decoder_inputs = KeraInput(shape=(None), dtype="int64", name="decoder_inputs")
        encoded_seq_inputs = KeraInput(shape=(None, embed_dim), name="decoder_state_inputs")

        x = PositionalEmbedding(sequence_length, vocab_size, embed_dim)(decoder_inputs)
        x = ShurlDecoder(embed_dim, latent_dim, num_heads)(x, encoded_seq_inputs)
        x = layers.Dropout(0.5)(x)

        decoder_outputs = layers.Dense(vocab_size, activation="softmax")(x)
        decoder = Model([decoder_inputs, encoded_seq_inputs], decoder_outputs)

        decoder_outputs = decoder([decoder_inputs, encoder_outputs])
        self.transformer = Model([encoder_inputs, decoder_inputs], decoder_outputs, name="transformer")
