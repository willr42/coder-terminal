import npyscreen
from filesystem import check_for_library_file


class ShelfView(npyscreen.Form):
    OK_BUTTON_TEXT = "EXIT?"

    def create(self):

        self.add(npyscreen.TitleText, name="Text:", value=f"{check_for_library_file()}")

    # Check for the existence of file.

    def afterEditing(self):
        self.parentApp.setNextForm(None)
