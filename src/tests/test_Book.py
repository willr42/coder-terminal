import pytest
from Book import Book


@pytest.fixture
def test_data():
    return {
        "author": "j.r.r. tolkien",
        "title": "the fellowship of the ring",
        "first_publish_year": 1954,
    }


class TestBook:
    def test_valid_book(self, test_data):
        """Tests a book with all fields populated."""

        test_book = Book(test_data)

        assert test_book.author == "j.r.r. tolkien"
        assert test_book.title == "the fellowship of the ring"
        assert test_book.first_publish_year == 1954

    def test_invalid_book(self, test_data):
        """Tests a book missing a field."""

        test_data["first_publish_year"] = 0
        test_book = Book(test_data)

        assert test_book.author == "j.r.r. tolkien"
        assert test_book.title == "the fellowship of the ring"
        assert test_book.first_publish_year == 0

    def test_edit_book(self, test_data):
        """Creates a book, then edits it, then tests that it has changed."""

        test_book = Book(test_data)
        test_book.update_book("author", "jeff bridges")

        assert test_book.author == "jeff bridges"

    def test_to_JSON(self, test_data):
        """Test the to_JSON method"""

        test_book = Book(test_data)
        test_json = test_book.to_JSON()

        assert test_json == test_data
