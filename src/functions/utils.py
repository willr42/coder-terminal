from rich.align import Align
from rich.console import Group
from rich.panel import Panel
from rich.table import Table

import os


def create_menu_table(table_key, **table_options):
    """Creates a table menu, and passes all other options through to Table constructor.

    Args:
        table_key (dict): key and description
        **table_options: kwargs accepted by `rich.table.Table` class.

    Returns:
        Table: Table ready to be printed by `rich.console.Console`.
    """

    table = Table(**table_options)
    table.add_column("Option", style="bold green")
    for key, value in table_key.items():
        table.add_row(key, value)
    return table


def menu_banner(heading, sub):
    """Creates a banner that features before each menu to explain the view.

    Args:
        heading (str): center-aligned heading
        sub (str): normal-aligned subtitle

    Returns:
        Panel: printable by `rich.console.Console`.
    """
    return Panel(
        Group(
            Align(
                heading,
                align="center",
            ),
            sub,
        ),
        expand=False,
    )


def clear_screen():
    os.system("cls" if os.name == "NT" else "clear")
