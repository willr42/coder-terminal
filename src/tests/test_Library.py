from ..Library import Library


class TestLibrary:
    def test_can_find_file_correctly(self, tmp_path):
        print(self)
        """Creates temp env with existing file and checks function correctly returns path."""
        temp_directory = tmp_path / "greatreads"
        temp_directory.mkdir()
        temp_file = temp_directory / "library.json"
        temp_file.touch()
        result = Library.initialise_library_file(tmp_path, temp_file)
        assert result
