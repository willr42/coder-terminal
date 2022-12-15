from textual.screen import Screen
from textual.containers import Vertical, Container
from textual.widgets import ListView, ListItem, Label, Header, Footer


class ShelfView(Screen):
    def compose(self):
        list_items = []
        for shelf in self.app.library.contents:
            list_items.append(ListItem(Label(f"{shelf.shelf_name}")))

        yield Label("Your Bookshelves", id="shelfTitle")
        yield Container(
            Vertical(ListView(*list_items), id="shelfListContainer"),
            id="shelfViewContainer",
        )

        yield Footer()
