from rich.console import Console
from exceptions import UserExited, UserInputEmptyException


def handle_user_input(prompt_str):
    console = Console()
    while True:
        try:
            user_input = collect_user_input(prompt_str)
        except UserInputEmptyException:
            console.print("❌ Sorry, your input was empty. Try again.")
        else:
            return user_input


def collect_user_input(prompt_str):
    user_input = input(prompt_str)
    if user_input == "":
        raise UserInputEmptyException
    if user_input == "\quit":
        raise UserExited
    else:
        return user_input
