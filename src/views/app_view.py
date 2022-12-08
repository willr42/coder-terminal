import npyscreen
from .shelf_view import ShelfView


class GreatReadsApp(npyscreen.NPSAppManaged):
    """Create the initial Application object."""

    def onStart(self):
        self.registerForm("MAIN", ShelfView())
