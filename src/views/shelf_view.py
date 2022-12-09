import npyscreen
from Library import Library


class ShelfView(npyscreen.Form):
    OK_BUTTON_TEXT = "EXIT?"

    def create(self):
        # Initialise a library
        library_path = Library.initialise_library_file()

        # Load library into Library object

        self.add(npyscreen.TitleText, name="Text:", value=f"{library_path}")

    def afterEditing(self):
        self.parentApp.setNextForm(None)
