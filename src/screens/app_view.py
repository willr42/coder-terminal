from textual.app import App
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import (
    Header,
    Footer,
    Input,
    Button,
    Static,
)

from Library import Library
from .shelf_view import ShelfView


class GreatReadsApp(App):
    """Create the initial Application object."""

    SCREENS = {"shelf": ShelfView()}
    CSS_PATH = "styles.css"

    def __init__(self):
        super().__init__()
        self.library = Library()

    def compose(self):
        """Create child widgets for the app."""

        yield Header()
        yield Footer()
        yield Container(
            Static(
                "Welcome to GreatReads. Ready to start managing your library?",
                id="welcomeMessage",
            ),
            Horizontal(
                Button("Get Started", id="start", variant="primary"),
                Button("Exit", id="exit"),
                id="welcomeButtonHolder",
            ),
        )

    def on_button_pressed(self, event):
        """Button press handler."""
        button_id = event.button.id
        if button_id == "start":
            self.push_screen("shelf")
        if button_id == "exit":
            self.exit()


class InputText(Input):
    pass
