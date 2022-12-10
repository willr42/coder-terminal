import platformdirs  # Using platformdirs, hopefully this should be cross-platform...


class Library:
    def __init__(self):
        self.json_path = self.initialise_library_file()
        pass

    def initialise_library_file(self, directory="greatreads", file="library.json"):
        """Checks for the existence of the greatreads library. If it doesn't exist, we create an empty instance of the file to write to later."""
        data_path = platformdirs.user_data_path().joinpath(directory)
        json_path = data_path.joinpath(file)
        try:
            if not data_path.exists():
                data_path.mkdir()
            if not json_path.is_file():
                json_path.touch()
            return json_path
        except Exception as exception:
            print(f"Something went wrong. {exception}")

    def load_library(self):
        """Loads the library from disk."""
        return {
            "shelves": [
                {
                    "shelf_name": "to read",
                    "books": [
                        {
                            "title": "harry potter and the chamber of secrets",
                            "published_on": "1990-02-04",
                            "author": "j.k. rowling",
                        },
                        {
                            "title": "going postal",
                            "published_on": "1900-01-01",
                            "author": "terry pratchett",
                        },
                    ],
                }
            ]
        }

    def save_library(self):
        """Save the library to disk as JSON."""
        pass
