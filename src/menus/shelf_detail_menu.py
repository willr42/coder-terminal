from rich.console import Console
from rich.table import Table

from exceptions import UserExited
from utils import create_menu_table, menu_banner
from user_input import handle_user_input


def shelf_detail_menu(library, active_shelf_name):
    """Main function that runs the shelf view menu."""
    shelf_detail_menu_choices = {
        "A": menu_add_book,
        "E": menu_edit_book,
        "R": menu_delete_book,
        "V": menu_view_book,
    }
    console = Console()

    console.print(
        menu_banner(
            heading="Shelf Detail View",
            sub="Here you can see all your books on the shelf.",
        )
    )

    active_shelf = library.get_shelf(active_shelf_name)

    print_shelf_detail_menu(active_shelf=active_shelf, console=console)

    while True:
        user_choice = handle_user_input("Choose your option: ").upper()
        if user_choice == "Q":
            raise UserExited
        if user_choice == "B":
            return False
        if user_choice not in shelf_detail_menu_choices.keys():
            print("Sorry, please select a valid choice.")
            continue
        shelf_detail_menu_choices[user_choice](library=library, console=console)
        print_shelf_detail_menu(active_shelf=active_shelf, console=console)


def print_shelf_detail_menu(active_shelf, console):
    """Present menu options."""

    print_shelf_contents(active_shelf=active_shelf, console=console)

    table_options = {
        "A": "Add a Book",
        "E": "Edit a Book",
        "R": "Remove a Book",
        "V": "View a Book's details",
        "B": "Go Back",
        "Q": "Quit",
    }

    console.print(create_menu_table(table_options, show_header=False, box=False))


def print_shelf_contents(active_shelf, console):
    """Print books in shelf."""
    table = Table()
    table.add_column("Book Title")
    table.add_column("Author")
    table.add_column("First Published")
    for book in active_shelf.contents:
        table.add_row(book.title, book.author, book.publication_year)
    console.print(table)


def menu_add_book(library, console):
    pass


def menu_edit_book(library, console):
    pass


def menu_delete_book(library, console):
    pass


def menu_view_book(library, console):
    pass
