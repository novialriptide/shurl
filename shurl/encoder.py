from keras import layers, Sequential


class ShurlEncoder(layers.Layer):  # type: ignore
    def __init__(self, embed_dim: int, dense_dim: int, heads_count: int) -> None:
        """
        @embed_dim: The dimensionality of the embedding space.
        @dense_dim: The dimensionality of the dense layer.
        @heads_count: The number of attention heads.
        """
        super().__init__()

        self.embed_dim = embed_dim
        self.dense_dim = dense_dim
        self.heads_count = heads_count

        self.multiattention_head = layers.MultiHeadAttention(num_heads=self.heads_count, key_dim=self.embed_dim)
        self.sequential_model = Sequential(
            layers=[
                layers.Dense(self.dense_dim, activation="relu"),
                layers.Dense(self.embed_dim),
            ]
        )

        self.layernorm_1 = layers.LayerNormalization()
        self.layernorm_2 = layers.LayerNormalization()
        self.supports_masking = True  # Derived from keras.layers.Layer
