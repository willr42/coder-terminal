from Book import Book


class Shelf:
    def __init__(self, data={}):
        self.contents = []
        self.shelf_name = "default"
        if data:
            self.shelf_name = data.get("shelf_name", "Default Shelf")
            self.add_initial_books(data)

    def __str__(self) -> str:
        return f"{self.shelf_name}"

    @property
    def length(self):
        return len(self.contents)

    def add_initial_books(self, data):
        if data.get("books", None):
            for book in data.get("books"):
                self.contents.append(Book(book))

    def add_new_book(self, new_book):
        if new_book:
            self.contents.append(new_book)

    def edit_book(self, book_title_to_edit, updates):
        """Edits a book by updating the fields in the supplied dictionary."""
        # Get a var that points to the book to edit
        for book in self.contents:
            if book.title == book_title_to_edit:
                book_to_edit = book

        # For all the updates provided, update the key
        for key in updates:
            book_to_edit.update_book(key, updates[key])

    def remove_book(self, book_to_remove):
        new_contents = [book for book in self.contents if book != book_to_remove]

        self.contents = new_contents
