import pytest
from Shelf import Shelf


@pytest.fixture
def test_data():
    return {
        "shelf_name": "Default Shelf",
        "books": [
            {
                "author": "j.r.r. tolkien",
                "title": "the fellowship of the ring",
                "first_publish_year": 1954,
            }
        ],
    }


class TestShelf:
    def test_can_create_empty_shelf(self):
        """Test if initialisation with empty shelf creates with default settings."""
        test_shelf = Shelf()
        assert test_shelf.length == 0
        assert test_shelf.shelf_name == "Default Shelf"

    def test_can_create_populated_shelf(self, test_data):
        """Test if initialisation with data works correctly."""

        test_shelf = Shelf(test_data)

        assert test_shelf.length == 1
        assert test_shelf.contents[0].author == "j.r.r. tolkien"

    def test_can_remove_book_from_populated_shelf(self, test_data):
        """Test removing a book from a shelf."""
        test_shelf = Shelf(test_data)
        book_to_remove = test_shelf.contents[0]
        test_shelf.remove_book(book_to_remove)
        assert test_shelf.length == 0

    def test_create_JSON_dictionary(self, test_data):
        """Test creation of a dictionary to be turned into JSON."""
        test_shelf = Shelf(test_data)
        to_test = test_shelf.to_JSON()
        assert test_data == to_test
