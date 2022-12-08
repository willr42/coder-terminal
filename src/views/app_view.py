import npyscreen


class GreatReadsApp(npyscreen.NPSAppManaged):
    """Create the initial Application object."""

    def onStart(self):
        self.registerForm("MAIN", MainForm())


class MainForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleText, name="Text:", value="Hello World!")

    def afterEditing(self):
        self.parentApp.setNextForm(None)
