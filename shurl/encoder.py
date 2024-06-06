from typing import Any
from keras import layers, Sequential, ops


class ShurlEncoder(layers.Layer):  # type: ignore
    def __init__(self, embed_dim: int, dense_dim: int, head_count: int) -> None:
        """
        @embed_dim: The dimensionality of the embedding space.
        @dense_dim: The dimensionality of the dense layer.
        @head_count: The number of attention heads.
        """
        super().__init__()

        self.embed_dim = embed_dim
        self.dense_dim = dense_dim
        self.head_count = head_count

        self.multiattention_head = layers.MultiHeadAttention(num_heads=self.head_count, key_dim=self.embed_dim)
        self.sequential_model = Sequential(
            layers=[
                layers.Dense(self.dense_dim, activation="relu"),
                layers.Dense(self.embed_dim),
            ]
        )

        self.layernorm_1 = layers.LayerNormalization()
        self.layernorm_2 = layers.LayerNormalization()
        self.supports_masking = True  # Derived from keras.layers.Layer

    def call(self, inputs: Any, mask: Any = None) -> Any:
        if mask is not None:
            padding_mask = ops.cast(mask[:, None, :], dtype="int32")
        else:
            padding_mask = None

        attention_output = self.multiattention_head(query=inputs, value=inputs, key=inputs, attention_mask=padding_mask)
        proj_input = self.layernorm_1(inputs + attention_output)
        proj_output = self.dense_proj(proj_input)

        return self.layernorm_2(proj_input + proj_output)
