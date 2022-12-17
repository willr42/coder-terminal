class Book:
    def __init__(self, data):
        self.title = data.get("title", "")
        self.author = data.get("author", "")
        self.first_publish_year = data.get("first_publish_year", 0)

    def __str__(self) -> str:
        return f"{self.title}, {self.author}, {self.first_publish_year}"

    @property
    def publication_year(self):
        return str(self.first_publish_year)

    def update_book(self, key_to_update, value_to_change):
        setattr(self, key_to_update, value_to_change)

    def to_JSON(self):
        return {
            "title": self.title,
            "author": self.author,
            "first_publish_year": self.first_publish_year,
        }
