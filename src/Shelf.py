from Book import Book


class Shelf:
    def __init__(self, data={}):
        self.contents = []
        self.shelf_name = "default"
        if data:
            self.shelf_name = data.get("shelf_name", "Default Shelf")
            self.add_initial_books(data)

    def add_initial_books(self, data):
        if data.get("books", None):
            for book in data.get("books"):
                self.contents.append(Book(book))
