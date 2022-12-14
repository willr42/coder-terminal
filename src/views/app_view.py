import npyscreen

from Library import Library
from views.shelf_view import AddShelfView, RenameShelfView, ShelfSelectView


class GreatReadsApp(npyscreen.NPSAppManaged):
    """Create the initial Application object."""

    def onStart(self):
        self.library = Library()
        self.addForm("MAIN", ShelfSelectView)
        self.addForm("ADD_SHELF", AddShelfView)
        self.addForm("RENAME_SHELF", RenameShelfView)
