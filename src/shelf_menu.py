from time import sleep
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from user_input import handle_user_input


def shelf_menu(library):
    """Main function that runs the shelf menu."""
    shelf_menu_choices = {
        "A": menu_add_shelf,
        "E": menu_edit_shelf,
        "R": menu_delete_shelf,
        "V": menu_view_shelf,
    }
    console = Console()

    console.print(
        Panel(
            "Shelf View\nHere you can operate on your shelves.",
            expand=False,
        )
    )

    print_shelf_menu(library=library, console=console)

    while True:
        user_choice = handle_user_input("Choose your option: ").upper()
        if user_choice == "Q":
            return False
        if user_choice not in shelf_menu_choices.keys():
            print("Sorry, please select a valid choice.")
            continue
        shelf_menu_choices[user_choice](library=library, console=console)


def print_shelf_menu(library, console):
    """Present menu options."""

    print_shelves(library=library, console=console)

    console.print("SHELF MENU", style="b u")
    table = Table(show_header=False, box=False)
    table.add_column("Option", style="bold green")
    table.add_row("V", "View Books on Shelf")
    table.add_row("A", "Add New Shelf")
    table.add_row("E", "Edit Shelf Name")
    table.add_row("R", "Remove Shelf")
    table.add_row("Q", "Quit")

    console.print(table)


def print_shelves(library, console):
    """Print shelves in library."""
    table = Table()
    table.add_column("Shelf Name")
    table.add_column("Book Count")
    for shelf in library.contents:
        table.add_row(shelf.shelf_name, str(shelf.length))
    console.print(table)


def menu_add_shelf(library, console):
    """Takes input for new shelf and passes it to global library object."""
    console.print(
        "Enter the name of the shelf you'd like to add, or \cancel to cancel", style="b"
    )
    new_shelf_name = handle_user_input("New Shelf: ")
    if new_shelf_name != "\cancel":
        library.add_shelf(new_shelf_name)
    print_shelf_menu(library, console)


def menu_edit_shelf(library, console):
    """Takes input for shelf to rename and passes to global library object."""
    console.print(
        "Which shelf would you like to rename? Or \cancel to cancel", style="b"
    )
    shelf_to_edit = handle_user_input("Edit Name: ")
    if shelf_to_edit != "\cancel":
        # If the shelf matches with one of the shelves in the library
        new_name = handle_user_input("Enter the new name of the shelf: ")
        library.rename_shelf(shelf_to_edit, new_name)
    print_shelf_menu(library, console)


def menu_delete_shelf(library, console):
    """Allows the user to delete their shelves, except for final shelf."""
    if library.shelf_count == 1:
        console.print("Sorry, you can't delete your final shelf.", style="red b")
        sleep(1)

    else:
    console.print("Which shelf would you like to delete?", style="b")
    delete_shelf_name = handle_user_input("Shelf to Delete: ")
    removed = library.remove_shelf(delete_shelf_name)
    if not removed:
        console.print("Sorry, I couldn't find that shelf.", style="red b")
        sleep(1)
    print_shelf_menu(library, console)


def menu_view_shelf(library, console):
    print("User wants to view")
    pass
    print_shelf_menu(library, console)
    return
