from Library import Library
from welcome_menu import welcome_menu
from shelf_menu import shelf_menu
from exceptions import UserExited
import sys


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
                shelf_response = shelf_menu(self.library)
                if not shelf_response:
                    raise UserExited
        except (UserExited, KeyboardInterrupt, EOFError):
            sys.exit(0)
        finally:
            self.cleanup()

    def cleanup(self):
        """Ensure safe shutdown."""
        print("Closing...")
        self.library.save_library()
