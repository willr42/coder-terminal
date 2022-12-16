from rich.table import Table


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
