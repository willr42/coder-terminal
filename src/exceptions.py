class UserInputEmptyException(Exception):
    """Raised when user input is empty."""

    pass


class UserExited(Exception):
    """Raised when user has given a quit function."""

    pass


class BookNotFound(Exception):
    """Raised when user has returned from adding a book unsuccessfully."""
