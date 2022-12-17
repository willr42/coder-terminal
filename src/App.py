import sys

from Library import Library
from menus.welcome_menu import welcome_menu
from menus.library_menu import library_menu
from exceptions import UserExited
from functions.utils import clear_screen


class App:
    def __init__(self):
        self.library = Library()

    def run(self):
        """Run main loop of the App."""
        clear_screen()
        try:
            while True:
                if not welcome_menu():
                    raise UserExited
                if not library_menu(self.library):
                    raise UserExited
        except (UserExited, KeyboardInterrupt, EOFError):
            sys.exit(0)
        finally:
            self.cleanup()

    def cleanup(self):
        """Ensure safe shutdown."""
        print("\nClosing...")
        self.library.save_library()
