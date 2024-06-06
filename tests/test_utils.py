from shurl.utils import delete_attributes


class TestUtils:
    def test_delete_attributes(self) -> None:
        sample_page = '<div class="sample-text" style="color: white">Hello!</div>'

        result = delete_attributes(sample_page)
        expected = "<div>Hello!</div>"

        assert result == expected
