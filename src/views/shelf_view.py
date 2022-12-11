import npyscreen


class ShelfView(npyscreen.Form):
    OK_BUTTON_TEXT = "EXIT?"

    def create(self):

        self.add(
            npyscreen.TitleText,
            name="Text:",
            value=f"{self.parentApp.library.json_data}",
        )

    def afterEditing(self):
        self.parentApp.setNextForm(None)
