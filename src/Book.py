class Book:
    def __init__(self, data):
        self.title = data.get("title", None)
        self.author = data.get("author", None)
        self.first_publish_year = data.get("first_publish_year", None)
