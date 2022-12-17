from Book import Book


class TestBook:
    def test_valid_book(self):
        """Tests a book with all fields populated."""
        data = {
            "author": "j.r.r. tolkien",
            "title": "the fellowship of the ring",
            "first_publish_year": 1954,
        }

        test_book = Book(data)

        assert test_book.author == "j.r.r. tolkien"
        assert test_book.title == "the fellowship of the ring"
        assert test_book.first_publish_year == 1954

    def test_invalid_book(self):
        """Tests a book missing a field."""
        data = {"author": "j.r.r. tolkien", "title": "the fellowship of the ring"}

        test_book = Book(data)
        assert test_book.author == "j.r.r. tolkien"
        assert test_book.title == "the fellowship of the ring"
        assert test_book.first_publish_year == 0

    def test_edit_book(self):
        """Creates a book, then edits it, then tests that it has changed."""
        data = {
            "author": "j.r.r. tolkien",
            "title": "the fellowship of the ring",
            "first_publish_year": 1954,
        }

        test_book = Book(data)
        test_book.update_book("author", "jeff bridges")
        assert test_book.author == "jeff bridges"
