class Book:
    def __init__(self, data):
        self.title = data.get("title", "")
        self.author = data.get("author", "")
        self.first_publish_year = data.get("first_publish_year", 0)

    @property
    def publication_year(self):
        return str(self.first_publish_year)

    def update_book(self, key_to_update, value_to_change):
        setattr(self, key_to_update, value_to_change)
