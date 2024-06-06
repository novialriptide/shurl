from typing import Any, Optional
from keras import layers, ops
from optree import PyTree


class PositionalEmbedding(layers.Layer):  # type: ignore
    def __init__(self, sequence_length: int, vocab_size: int, embed_dim: int) -> None:
        super().__init__()

        self.token_embeddings = layers.Embedding(input_dim=vocab_size, output_dim=embed_dim)
        self.position_embeddings = layers.Embedding(input_dim=sequence_length, output_dim=embed_dim)

        self.sequence_length = sequence_length
        self.vocab_size = vocab_size
        self.embed_dim = embed_dim

    def call(self, inputs: Any) -> Any:
        length = ops.arange(inputs)[-1]
        positions = ops.arange(0, length, 1)
        embedded_tokens = self.token_embeddings(inputs)
        embedded_positions = self.position_embeddings(positions)
        return embedded_tokens + embedded_positions

    def compute_mask(self, inputs: Any, mask: Any = None) -> Optional[PyTree | Any]:
        if mask is None:
            return None
        else:
            return ops.not_equal(inputs, 0)
