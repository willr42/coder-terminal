from pathlib import Path
import platformdirs  # Using platformdirs, hopefully this should be cross-platform...
import orjson


class Library:
    def __init__(self, directory="greatreads", file="library.json"):
        self.json_path = self.initialise_library_file(directory, file)
        data = self.deserialize_library()
        self.create_library(data)

    def initialise_library_file(self, directory, file):
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

    def deserialize_library(self):
        """Loads the library from disk."""

        library_path = self.json_path

        library_path = Path("/home/willr/development/coder-terminal/dummydata.json")

        try:
            with open(library_path, "r") as file:
                json_data = orjson.loads(file.read())
                return json_data

        except FileNotFoundError:
            exit(1)

    def create_library(self, data):
        """Creates the Shelves and Books inside the library."""
        self.json_data = data
        pass

    def save_library(self):
        """Save the library to disk as JSON."""
        pass
