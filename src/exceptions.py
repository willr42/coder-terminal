class UserInputEmptyException(Exception):
    """Raised when user input is empty."""


class UserExited(Exception):
    """Raised when user has given a quit function."""


class NetworkConnectivityError(Exception):
    """Raised when the internet connectivity doesn't work."""
