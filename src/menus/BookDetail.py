# Types
from rich.console import Console
from rich.text import Text

from Book import Book
from exceptions import BookNotFound
from functions.SearchHandler import SearchHandler
from functions.user_input import (
    menu_option_input,
    handle_string_input,
    handle_int_input,
)
from functions.utils import menu_banner, create_menu_table

# This is implemented as a class as I need various sub-class versions of this for adding & editing.
class _BookDetailView:
    def __init__(self, console: Console):
        self.console = console

    def print_intro(self):
        self.console.print(
            menu_banner("Book Detail View", "See the details of your book.")
        )


class BookDetailAdd(_BookDetailView):
    """View for adding a new book."""

    def __init__(self, active_shelf, console):
        self.active_shelf = active_shelf
        super().__init__(console)

    def add_book(self):
        """Main method for adding a book. Presents menu options and handles input."""

        self.add_screen_intro()

        add_book_options = {"M": self.add_book_manually, "S": self.add_book_search}

        while True:
            user_choice = menu_option_input("Choose your option: ")
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
            Text("New book added:", style="green", end=""),
            f"{book_title} by {author_name}, first published in {first_published}",
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
        while True:
            self.console.print("Select your result from 1-10")
            chosen_result = handle_int_input("Selection: ")
            if 1 > chosen_result < 10:
                continue
            break
        found_book = search_handler.make_user_choice(chosen_result)
        return found_book


class BookDetailEdit(_BookDetailView):
    def __init__(self, console: Console, book):
        super().__init__(console)
        self.book = book

    def edit_book(self):
        """Main method for editing a book."""

        self.edit_screen_intro()

        edit_book_options = {"T": "title", "A": "author", "D": "first_publish_year"}

        while True:
            user_choice = menu_option_input("Choose your option: ")
            if user_choice == "B":
                return False
            if user_choice not in edit_book_options.keys():
                print("Sorry, please select a valid choice.")
                continue
            if user_choice == "D":
                new_field_info = handle_int_input("Update: ")
            else:
                new_field_info = handle_string_input("Update: ")
            self.book.update_book(
                key_to_update=edit_book_options[user_choice],
                value_to_change=new_field_info,
            )
            self.edit_screen_intro()

    def edit_screen_intro(self):
        """Prints instructional information."""
        self.print_intro()

        table_options = {
            "T": "Edit title",
            "A": "Edit author name",
            "D": "Edit first publish date",
            "B": "Go Back",
        }

        self.console.print("Edit Mode", style="i green")
        self.console.print(
            create_menu_table(table_key=table_options, show_header=False, box=False)
        )
