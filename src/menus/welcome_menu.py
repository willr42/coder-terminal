# Library imports
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Project imports
from functions.user_input import menu_option_input


def welcome_menu():
    print_welcome_menu()

    main_menu_choices = {"1": True, "2": False}

    while True:
        user_choice = menu_option_input("Choose your option: ")
        if user_choice not in main_menu_choices.keys():
            print("Sorry, please select a valid choice.")
            continue
        elif user_choice == "1":
            return True
        return False


def print_welcome_menu():
    console = Console()
    console.print(
        Panel(
            "Welcome to GreatReads!\nThe new way to manage your library of books in the terminal.",
            expand=False,
        )
    )
    console.print("MAIN MENU", style="b u")
    table = Table(show_header=False, box=False)
    table.add_column("Option", style="bold green")
    table.add_row("1", "Start")
    table.add_row("2", "Exit")
    console.print(table)
