from shurl.utils import preprocess


class TestPreprocessing:
    def test_excerpt1(self) -> None:
        value = preprocess(
            """I glanced at my arm readouts (This is a test string that should
not be in the final output). My oxygen reserve plummeted while I watched,
so I stopped watching. (Excerpt from Andy Weir's "Artemis")"""
        )
        assert value == [
            "i",
            "glanced",
            "at",
            "my",
            "arm",
            "readouts",
            "my",
            "oxygen",
            "reserve",
            "plummeted",
            "while",
            "i",
            "watched",
            "so",
            "i",
            "stopped",
            "watching",
        ]
