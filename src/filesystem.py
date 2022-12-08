import platformdirs


def check_for_library_file():
    """Checks for the existence of the greatreads library. If it doesn't exist, we create an empty instance of the file to write to later."""
    data_path = platformdirs.user_data_path().joinpath("greatreads")
    json_path = data_path.joinpath("library.json")
    try:
        if not data_path.exists():
            data_path.mkdir()
        if not json_path.is_file():
            json_path.touch()
        return json_path
    except Exception as exception:
        print(f"Something went wrong. {exception}")
