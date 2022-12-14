from pathlib import Path
from Shelf import Shelf
import platformdirs  # Using platformdirs, hopefully this should be cross-platform...
import orjson


class Library:
    def __init__(self, directory="greatreads", file="library.json"):
        self.contents = []
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

        library_path = Path.home() / "development" / "coder-terminal" / "dummydata.json"

        try:
            with open(library_path, "r") as file:
                cache = file.read()
                # Catch if there's an empty JSON file
                if cache:
                    json_data = orjson.loads(cache)
                    return json_data
        except FileNotFoundError:
            exit(1)

    # TODO Missing step here. Add a validate data section – we want to make sure the JSON file hasn't been changed somehow between sessions.

    def create_library(self, data):
        """Creates the Shelves and Books inside the library."""
        # If data exists, they've run before, so construct the shelves.
        if data:
            for shelf in data.get("shelves"):
                self.contents.append(Shelf(shelf))
        # If no data, we just create an empty Shelf object to work with.
        else:
            self.add_shelf("Default Shelf")

    def add_shelf(self, shelf_name):
        self.contents.append(Shelf(data={"shelf_name": shelf_name}))

    def rename_shelf(self, old_shelf_name, new_shelf_name):
        for shelf in self.contents:
            if shelf.shelf_name == old_shelf_name:
                shelf.shelf_name = new_shelf_name

    def save_library(self):
        """Save the library to disk as JSON."""
        pass
