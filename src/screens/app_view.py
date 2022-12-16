from textual.screen import Screen
from textual.app import App
from textual.containers import Container, Horizontal, Grid
from textual.widgets import (
    Header,
    Footer,
    Button,
    Static,
)

from Library import Library
from .shelf_view import ShelfView, BookView


class GreatReadsApp(App):
    """Create the initial Application object."""

    SCREENS = {"shelf": ShelfView(), "book_overview": BookView()}
    CSS_PATH = "styles.css"
    BINDINGS = [("escape", "request_quit", "Quit")]

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
                id="welcomeButtonHolder",
            ),
        )

    def on_button_pressed(self, event):
        """Button press handler."""
        button_id = event.button.id
        if button_id == "start":
            self.push_screen("shelf")

    def action_request_quit(self):
        self.push_screen(QuitScreen())


class QuitScreen(Screen):
    """Taken from the official documentation."""

    def compose(self):
        yield Container(
            Grid(
                Static("Are you sure you want to quit?", id="quitQuestion"),
                Button("Quit", variant="error", classes="quitButton", id="quit"),
                Button("Cancel", variant="primary", classes="quitButton"),
                id="quitDialog",
            ),
            id="quitDialogWrapper",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            # TODO save app ehre
            self.app.exit()
        else:
            self.app.pop_screen()
