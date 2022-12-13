class Book:
    def __init__(self, data):
        self.title = data.get("title", None)
        self.author = data.get("author", None)
        self.first_publish_year = data.get("first_publish_year", None)

    def update_book(self, key_to_update, value_to_change):
        setattr(self, key_to_update, value_to_change)
