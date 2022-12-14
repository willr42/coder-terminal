from time import sleep
from rich.console import Console
from rich.table import Table

from menus.shelf_detail_menu import shelf_detail_menu
from functions.user_input import menu_option_input, handle_string_input
from functions.utils import create_menu_table, menu_banner


def library_menu(library):
    """Main function that runs the library menu."""
    library_menu_choices = {
        "A": library_menu_add_shelf,
        "E": library_menu_edit_shelf,
        "R": library_menu_delete_shelf,
        "V": library_menu_view_shelf,
    }
    console = Console()

    console.print(
        menu_banner("Library View", "Here you can make changes to your shelves.")
    )

    print_library_menu(library=library, console=console)

    while True:
        user_choice = menu_option_input("Choose your option: ")
        # Handle direct quit order
        if user_choice == "Q":
            return False
        # Check for missing command
        if user_choice not in library_menu_choices.keys():
            print("Sorry, please select a valid choice.")
            continue
        library_menu_choices[user_choice](library=library, console=console)
        print_library_menu(library=library, console=console)
        # If this returns False, they've selected quit


def print_library_menu(library, console):
    """Present menu options."""

    print_shelves(library=library, console=console)

    console.print("SHELF MENU", style="b u")
    table_options = {
        "V": "View Books on Shelf",
        "A": "Add New Shelf",
        "E": "Edit Shelf Name",
        "R": "Remove Shelf",
        "Q": "Quit",
    }
    console.print(create_menu_table(table_options, show_header=False, box=False))


def print_shelves(library, console):
    """Print shelves in library."""
    table = Table()
    table.add_column("Shelf Name")
    table.add_column("Book Count")
    for shelf in library.contents:
        table.add_row(str(shelf), str(shelf.length))
    console.print(table)


def library_menu_add_shelf(library, console):
    """Takes input for new shelf and passes it to global library object."""
    console.print(
        "Enter the name of the shelf you'd like to add, or \cancel to cancel", style="b"
    )
    new_shelf_name = handle_string_input("New Shelf: ")
    if new_shelf_name != "\cancel":
        library.add_shelf(new_shelf_name)


def library_menu_edit_shelf(library, console):
    """Takes input for shelf to rename and passes to global library object."""
    console.print(
        "Which shelf would you like to rename? Or \cancel to cancel", style="b"
    )
    shelf_to_edit = handle_string_input("Edit Name: ")
    if shelf_to_edit != "\cancel":
        # If the shelf matches with one of the shelves in the library
        new_name = handle_string_input("Enter the new name of the shelf: ")
        library.rename_shelf(shelf_to_edit, new_name)


def library_menu_delete_shelf(library, console):
    """Allows the user to delete their shelves, except for final shelf."""
    if library.shelf_count == 1:
        console.print("Sorry, you can't delete your final shelf.", style="red b")
        sleep(1)

    else:
        console.print("Which shelf would you like to delete?", style="b")
        delete_shelf_name = handle_string_input("Shelf to Delete: ")
        removed = library.remove_shelf(delete_shelf_name)
        if not removed:
            console.print("Sorry, I couldn't find that shelf.", style="red b")
            sleep(1)


def library_menu_view_shelf(library, console):
    """Activates individual shelf view."""
    # Take input for shelf name
    console.print("Which shelf would you like to view?", style="b")
    shelf_to_view = handle_string_input("Shelf to View: ")
    # If shelf doesn't exist, back to menu
    if not library.get_shelf(shelf_to_view):
        console.print(f"Sorry, the {shelf_to_view} shelf doesn't exist.")
        sleep(1)
    else:
        while True:
            shelf_detail_view_response = shelf_detail_menu(
                library=library, active_shelf_name=shelf_to_view
            )
            # If this returns, we want to come back to the main shelf menu
            if not shelf_detail_view_response:
                break
