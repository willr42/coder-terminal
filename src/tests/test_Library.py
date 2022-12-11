from ..Library import Library
import platformdirs


class TestLibrary:
    def test_can_find_file_correctly(self, tmp_path):
        """Creates temp env with existing file and checks function correctly returns path."""
        temp_directory = tmp_path / "greatreads"
        temp_directory.mkdir()
        temp_file = temp_directory / "library.json"
        temp_file.touch()
        result = Library(tmp_path, temp_file)
        assert result

    def test_default_filepath(self):
        """Test if Library creates default file without any arguments."""
        result = Library()
        assert (
            result.json_path
            == platformdirs.user_data_path() / "greatreads" / "library.json"
        )
