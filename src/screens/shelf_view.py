from textual.screen import Screen
from textual.containers import Vertical, Container, Grid, Horizontal
from textual.widgets import ListView, ListItem, Label, Footer, Button


class ShelfView(Screen):
    def compose(self):
        yield Footer()

        list_items = []
        for index, shelf in enumerate(self.app.library.contents):
            list_items.append(
                ShelfListItem(Label(f"{shelf.shelf_name}"), id=f"shelf_{str(index)}")
            )

        yield Grid(
            Container(
                Label("Your Bookshelves", id="shelfTitleText"),
                Label("Click one to get started."),
                id="shelfTitleContainer",
            ),
            Container(
            Vertical(ListView(*list_items), id="shelfListContainer"),
            id="shelfViewContainer",
            ),
            Horizontal(
                Button("Add", id="addShelfButton"),
                Button("Rename", id="renameShelfButton"),
                Button("Remove", id="removeShelfButton"),
                id="shelfButtonContainer",
            ),
            id="shelfGrid",
        )

        yield Footer()
