import pytest
from Library import Library
import platformdirs


@pytest.fixture
def temporary_location(tmp_path):
    """Creates a temporary library location to ensure testing doesn't affect files."""

    temp_directory = tmp_path / "greatreads"
    temp_directory.mkdir()
    temp_file = temp_directory / "library.json"
    temp_file.touch()
    return {"temp_path": tmp_path, "temp_file": temp_file}


class TestLibrary:
    def test_can_find_file_correctly(self, temporary_location):
        """Creates temp env with existing file and checks function correctly returns path."""

        result = Library(
            temporary_location["temp_path"], temporary_location["temp_file"]
        )
        assert result

    def test_default_filepath(self):
        """Test if Library creates default file without any arguments."""

        result = Library()
        assert (
            result.json_path
            == platformdirs.user_data_path() / "greatreads" / "library.json"
        )

    def test_add_shelf(self, temporary_location):
        """Tests that you can add a shelf to a library."""

        temp_library = Library(
            temporary_location["temp_path"], temporary_location["temp_file"]
        )
        temp_library.add_shelf("new test shelf")
        assert temp_library.get_shelf("new test shelf").shelf_name == "new test shelf"
        assert temp_library.shelf_count == 2

    def test_rename_shelf(self, temporary_location):
        """Tests you can rename a shelf."""

        temp_library = Library(
            temporary_location["temp_path"], temporary_location["temp_file"]
        )
        temp_library.add_shelf("new test shelf")
        temp_library.rename_shelf("new test shelf", "new name")
        found_shelf = temp_library.get_shelf("new name")
        assert found_shelf.shelf_name == "new name"

    def test_remove_shelf(self, temporary_location):
        """Tests you can remove a single shelf from a library."""

        temp_library = Library(
            temporary_location["temp_path"], temporary_location["temp_file"]
        )
        temp_library.add_shelf("new test shelf")
        temp_library.remove_shelf("new test shelf")
        assert temp_library.shelf_count == 1
