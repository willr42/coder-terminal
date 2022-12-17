import sys

from Library import Library
from menus.welcome_menu import welcome_menu
from menus.library_menu import library_menu
from exceptions import UserExited


class App:
    def __init__(self):
        self.library = Library()

    def run(self):
        """Run main loop of the App."""
        try:
            while True:
                main_response = welcome_menu()
                if not main_response:
                    raise UserExited
                shelf_response = library_menu(self.library)
                if not shelf_response:
                    raise UserExited
        except (UserExited, KeyboardInterrupt, EOFError):
            sys.exit(0)
        finally:
            self.cleanup()

    def cleanup(self):
        """Ensure safe shutdown."""
        print("\nClosing...")
        self.library.save_library()
