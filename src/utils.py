from rich.table import Table

# console.print("SHELF MENU", style="b u")
# table = Table(show_header=False, box=False)
# table.add_column("Option", style="bold green")
# table.add_row("V", "View Books on Shelf")
# table.add_row("A", "Add New Shelf")
# table.add_row("E", "Edit Shelf Name")
# table.add_row("R", "Remove Shelf")
# table.add_row("Q", "Quit")

# console.print(table)
def create_menu_table(table_key, **table_options):
    table = Table(**table_options)
    table.add_column("Option", style="bold green")
    for key, value in table_key.items():
        table.add_row(key, value)
    return table
