from rich.console import Console

from Book import Book
from exceptions import BookNotFound
from user_input import menu_option_input, handle_string_input, handle_int_input
from utils import menu_banner, create_menu_table

# This is implemented as a class as I need various sub-class versions of this for add, edit and viewing.
class _BookDetailView:
    def __init__(self, active_shelf, console: Console):
        self.active_shelf = active_shelf
        self.console = console

    def print_intro(self):
        self.console.print(
            menu_banner("Book Detail View", "See the details of your book.")
        )


class BookDetailAdd(_BookDetailView):
    """View for adding a new book."""

    def __init__(self, active_shelf, console):
        super().__init__(active_shelf, console)

    def add_book(self):
        """Main method for adding a book. Presents menu options and handles input."""

        self.add_screen_intro()

        add_book_options = {"M": self.add_book_manually, "S": self.add_book_search}

        while True:
            user_choice = menu_option_input("Choose your option: ").upper()
            if user_choice == "B":
                return False
            if user_choice not in add_book_options.keys():
                print("Sorry, please select a valid choice.")
                continue
            try:
                book_to_add = add_book_options[user_choice]()
                self.active_shelf.add_new_book(book_to_add)
                self.add_screen_intro()
            except BookNotFound:
                self.console.print("Cancelling adding book.", style="pink")
                break

    def add_screen_intro(self):
        """Prints instructional information."""
        self.print_intro()

        table_options = {
            "M": "Add book manually",
            "S": "Search for book by title",
            "B": "Back",
        }

        self.console.print("Add Mode\nAdd manually or search.", style="i green")
        self.console.print(
            create_menu_table(table_key=table_options, show_header=False, box=False)
        )

    def add_book_manually(self) -> Book:
        self.console.print("Manual Mode", style="i green underline")
        book_title = handle_string_input("Book title: ")
        author_name = handle_string_input("Author name: ")
        first_published = handle_int_input("Year first published: ")
        self.console.print(
            f"New book added: {book_title} by {author_name}, first published in {first_published}"
        )

        return Book(
            {
                "title": book_title,
                "author": author_name,
                "first_publish_year": first_published,
            }
        )

    def add_book_search(self) -> Book:
        self.console.print("Search Mode", style="i blue underline")
        term_to_search = handle_string_input("Search term: ")
        search_handler = SearchHandler(term_to_search)
        self.console.print(search_handler.search_results)
