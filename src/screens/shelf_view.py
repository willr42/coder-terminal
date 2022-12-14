from textual.screen import Screen
from textual.widgets import ListView, ListItem, Label, Header, Footer


class ShelfView(Screen):
    def compose(self):
        yield Header()
        list_items = []
        for shelf in self.app.library.contents:
            list_items.append(ListItem(Label(f"{shelf.shelf_name}")))
        yield ListView(*list_items)
        yield Footer()
