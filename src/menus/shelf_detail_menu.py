# Library imports
from time import sleep
from rich.console import Console
from rich.table import Table

# Project imports
from exceptions import UserExited
from menus.BookDetail import BookDetailAdd, BookDetailEdit
from functions.user_input import menu_option_input, handle_string_input
from functions.utils import create_menu_table, menu_banner


def shelf_detail_menu(library, active_shelf_name):
    """Main function that runs the shelf view menu."""
    shelf_detail_menu_choices = {
        "A": menu_add_book,
        "E": menu_edit_book,
        "R": menu_delete_book,
        "S": menu_sort_shelf,
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
        user_choice = menu_option_input("Choose your option: ")
        if user_choice == "Q":
            raise UserExited
        if user_choice == "B":
            return False
        if user_choice not in shelf_detail_menu_choices.keys():
            print("Sorry, please select a valid choice.")
            continue
        shelf_detail_menu_choices[user_choice](
            active_shelf=active_shelf, console=console
        )
        print_shelf_detail_menu(active_shelf=active_shelf, console=console)


def print_shelf_detail_menu(active_shelf, console):
    """Present menu options."""

    print_shelf_contents(active_shelf=active_shelf, console=console)

    table_options = {
        "A": "Add a Book",
        "E": "Edit a Book",
        "R": "Remove a Book",
        "S": "Sort Shelf",
        "B": "Go Back",
        "Q": "Quit",
    }

    console.print(create_menu_table(table_options, show_header=False, box=False))


def print_shelf_contents(active_shelf, console):
    """Print books in shelf."""
    table = Table()
    if active_shelf.length == 0:
        table.show_header = False
        table.add_row("Empty shelf!", style="italic")
    else:
        table.add_column("Book Title")
        table.add_column("Author")
        table.add_column("First Published")
        for book in active_shelf.contents:
            table.add_row(book.title, book.author, book.publication_year)
    console.print(table)


def menu_add_book(active_shelf, console):
    """Opens the add menu screen."""
    BookDetailAdd(active_shelf=active_shelf, console=console).add_book()


def menu_edit_book(active_shelf, console):
    """Asks for user input and if book is found, opens the edit menu."""
    if active_shelf.length == 0:
        console.print("Sorry, there are no books to edit.", style="b")
        sleep(1)
    else:
        console.print("Which book would you like to edit?", style="b")
        book = find_book_in_shelf(active_shelf=active_shelf)
        if not book:
            console.print(f"Sorry, I can't find that book.", style="red b")
            return
        BookDetailEdit(console=console, book=book).edit_book()


def menu_delete_book(active_shelf, console):
    """Asks for user input and if book is found, removes the book."""
    if active_shelf.length == 0:
        console.print("Sorry, there are no books to delete.", style="b")
        sleep(1)
    else:
        console.print("Which book would you like to delete?", style="b")
        book = find_book_in_shelf(active_shelf=active_shelf)
        if not book:
            console.print(f"Sorry, I can't find that book.", style="red b")
            return
        active_shelf.remove_book(book)


def menu_sort_shelf(active_shelf, console):
    """Prints a menu and sorts depending on user input."""
    print_sort_menu(console)
    user_choice = menu_option_input("Sort by what?")
    if user_choice == "T":
        active_shelf.contents.sort(key=lambda book: book.title)
    if user_choice == "A":
        active_shelf.contents.sort(key=lambda book: book.author)
    if user_choice == "Y":
        active_shelf.contents.sort(
            key=lambda book: book.first_publish_year, reverse=True
        )


def print_sort_menu(console):
    """Prints the sort menu."""
    sort_options = {
        "T": "Sort by Title",
        "A": "Sort by Author",
        "Y": "Sort by First Published",
    }
    console.print(create_menu_table(sort_options, show_header=False, box=False))


def find_book_in_shelf(active_shelf):
    "Searches through a shelf to find a book."
    book_to_find = handle_string_input("Book: ")
    for book in active_shelf.contents:
        if book_to_find == book.title:
            return book
    return False
