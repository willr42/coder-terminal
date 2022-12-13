import npyscreen

from Library import Library
from views.shelf_view import ShelfEditView, ShelfSelectView


class GreatReadsApp(npyscreen.NPSAppManaged):
    """Create the initial Application object."""

    def onStart(self):
        self.library = Library()
        self.addForm("MAIN", ShelfSelectView)
        self.addForm("EDIT_SHELVES", ShelfEditView)
