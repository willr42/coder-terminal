import npyscreen


class ShelfSelectView(npyscreen.Form):
    OK_BUTTON_TEXT = "EXIT?"

    def create(self):
        # pass in the shelves to be displayed
        self.add(
            ShelfList,
            values=self.parentApp.library.contents,
            allow_filtering=False,
            max_height=10,
            scroll_exit=True,
        )

        self.add(EditShelves, name="Edit Shelves")

    def afterEditing(self):
        self.parentApp.setNextForm(None)


class ShelfList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(ShelfList, self).__init__(*args, **keywords)

    # change how each shelf is displayed
    def display_value(self, vl):
        return vl.shelf_name.title()

    # change the action on keypress
    def actionHighlighted(self, act_on_this, key_press):
        pass


class EditShelves(npyscreen.Button):
    def __init__(self, screen, *args, **keywords):
        super().__init__(screen, *args, **keywords)

    def whenToggled(self):
        print("Hello")
