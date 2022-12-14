from Book import Book


class Shelf:
    def __init__(self, data: dict = None):
        if not data:
            data = {}

        self.contents = []
        self.shelf_name = "Default Shelf"

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

    def remove_book(self, book_to_remove):
        new_contents = [book for book in self.contents if book != book_to_remove]

        self.contents = new_contents

    def to_JSON(self):
        json_dict = {"shelf_name": self.shelf_name, "books": []}
        for book in self.contents:
            json_dict["books"].append(book.to_JSON())

        return json_dict
