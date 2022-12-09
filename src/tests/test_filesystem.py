from ..filesystem import check_for_library_file


def test_can_find_file_correctly(self, tmp_path):
    """Creates temp env with existing file and checks function correctly returns path."""
    temp_directory = tmp_path / "greatreads"
    temp_directory.mkdir()
    temp_file = temp_directory / "library.json"
    temp_file.touch()
    result = check_for_library_file(tmp_path, temp_file)
    assert result
