# Library imports
import platformdirs  # Using platformdirs, hopefully this should be cross-platform...
import orjson

# Project imports
from pathlib import Path
from Shelf import Shelf


class Library:
    def __init__(self, directory="greatreads", file="library.json"):
        self.contents = []
        self.json_path = self.initialise_library_file(directory, file)
        data = self.deserialize_library()
        self.create_library(data)

    @property
    def shelf_count(self):
        return len(self.contents)

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
            print(
                f"Sorry, something completely unexpected went wrong: {exception}. Please file a bug on GitHub."
            )
            exit(2)

    def deserialize_library(self):
        """Loads the library from disk."""

        library_path = self.json_path

        library_path = (
            Path.home()
            / "development"
            / "coderacademy"
            / "coder-terminal"
            / "dummydata.json"
        )

        try:
            with open(library_path, "r") as file:
                cache = file.read()
                # Catch if there's an empty JSON file
                if cache:
                    json_data = orjson.loads(cache)
                    return json_data
        except FileNotFoundError as exception:
            print(
                f"Something's gone horribly wrong. Exception: {exception}. Please file a bug on GitHub."
            )
            exit(1)

    def create_library(self, data):
        """Creates the Shelves and Books inside the library."""
        # If data exists, they've run before, so construct the shelves.
        if data:
            for shelf in data.get("shelves"):
                self.contents.append(Shelf(shelf))
        # If no data, we just create an empty Shelf object to work with.
        else:
            self.contents.append(Shelf(data={"shelf_name": "Default Shelf"}))

    def add_shelf(self, shelf_name):
        if shelf_name == "":
            return "Cannot create an empty shelf."
        else:
            self.contents.append(Shelf(data={"shelf_name": shelf_name}))

    def get_shelf(self, shelf_name):
        for shelf in self.contents:
            if shelf.shelf_name == shelf_name:
                return shelf

    def rename_shelf(self, old_shelf_name, new_shelf_name):
        for shelf in self.contents:
            if shelf.shelf_name == old_shelf_name:
                shelf.shelf_name = new_shelf_name

    def remove_shelf(self, shelf_name):
        new_contents = []
        found = False

        for shelf in self.contents:
            if shelf.shelf_name == shelf_name:
                found = True
            else:
                new_contents.append(shelf)

        # If shelf is found, we use the new_contents object
        if found:
            self.contents = new_contents

        return found

    def save_library(self):
        """Save the library to disk as JSON."""
        print("saved library")
