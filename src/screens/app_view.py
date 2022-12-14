from textual.app import App
from textual.widgets import (
    Header,
    Footer,
    Input,
    Button,
    Static,
    ListItem,
    ListView,
    Label,
)

from Library import Library
from .shelf_view import ShelfView


class GreatReadsApp(App):
    """Create the initial Application object."""

    SCREENS = {"shelf": ShelfView()}

    def __init__(self):
        super().__init__()
        self.library = Library()

    def compose(self):
        """Create child widgets for the app."""
        yield Header()
        yield Static("Welcome to GreatReads. Ready to start managing your library?")
        yield Button("Get Started", id="start", variant="primary")
        yield Footer()

    def on_button_pressed(self, event):
        button_id = event.button.id
        if button_id == "start":
            self.push_screen("shelf")

    def on_static_clicked(self, event):
        print(event.handler_name)


class InputText(Input):
    pass
