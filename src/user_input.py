from rich.console import Console
from exceptions import UserExited, UserInputEmptyException


def handle_string_input(prompt_str):
    console = Console()
    while True:
        try:
            user_input = collect_user_input(prompt_str)
        except UserInputEmptyException:
            console.print("❌ Sorry, your input was empty. Try again.")
        else:
            return user_input


def handle_int_input(prompt_str):
    console = Console()
    while True:
        try:
            user_input = collect_user_input(prompt_str)
            int(user_input)
        except ValueError:
            console.print("❌ Sorry, your input wasn't a valid number. Try again.")
        except UserInputEmptyException:
            console.print("❌ Sorry, your input was empty. Try again.")
        else:
            return int(user_input)


def menu_option_input(prompt_str):
    console = Console()
    while True:
        try:
            user_input = collect_user_input(prompt_str)
        except UserInputEmptyException:
            console.print("❌ Sorry, your input was empty. Try again.")
        else:
            return user_input.upper()


def collect_user_input(prompt_str):
    user_input = input(prompt_str)
    if user_input == "":
        raise UserInputEmptyException
    if user_input == "\quit":
        raise UserExited
    else:
        return user_input
