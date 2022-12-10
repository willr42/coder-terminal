import npyscreen

from Library import Library
from .shelf_view import ShelfView


class GreatReadsApp(npyscreen.NPSAppManaged):
    """Create the initial Application object."""

    def onStart(self):
        self.library = Library()
        self.addForm("MAIN", ShelfView)
