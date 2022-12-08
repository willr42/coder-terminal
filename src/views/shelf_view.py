import npyscreen
from fileloader import file_loader


class ShelfView(npyscreen.Form):
    OK_BUTTON_TEXT = "EXIT?"

    def create(self):

        self.add(npyscreen.TitleText, name="Text:", value=f"{file_loader()}")

    # Check for the existence of file.

    def afterEditing(self):
        self.parentApp.setNextForm(None)
