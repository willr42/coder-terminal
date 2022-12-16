from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from user_input import handle_user_input


def shelf_menu(library):
    shelf_menu_choices = {
        "A": menu_add_shelf,
        "E": menu_edit_shelf,
        "R": menu_delete_shelf,
        "V": menu_view_shelf,
    }
    console = Console()

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
    console.print(
        Panel(
            "Shelf View\nHere you can operate on your shelves.",
            expand=False,
        )
    )

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
    table = Table()
    table.add_column("Shelf Name")
    table.add_column("Book Count")
    for shelf in library.contents:
        table.add_row(shelf.shelf_name, str(shelf.length))
    console.print(table)


def menu_add_shelf(library, console):
    console.print("Enter the name of the shelf you'd like to add", style="b")
    new_shelf_name = handle_user_input("New Shelf: ")
    library.add_shelf(new_shelf_name)
    print_shelf_menu(library, console)


def menu_edit_shelf(library, console):
    print("User wants to edit")
    pass


def menu_delete_shelf(library, console):
    print("User wants to delete")
    pass


def menu_view_shelf(library, console):
    print("User wants to view")
    pass
