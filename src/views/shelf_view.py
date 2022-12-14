import npyscreen


class ShelfSelectView(npyscreen.ActionFormMinimal):
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

        self.add(
            npyscreen.ButtonPress,
            name="Add New Shelf",
            when_pressed_function=self.change_to_add,
        )

        self.add(
            npyscreen.ButtonPress,
            name="Rename Shelves",
            when_pressed_function=self.change_to_rename,
        )

    def change_to_add(self):
        self.parentApp.switchForm("ADD_SHELF")

    def change_to_rename(self):
        self.parentApp.switchForm("RENAME_SHELF")

    def on_ok(self):
        self.parentApp.library.save_library()
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


class AddShelfView(npyscreen.ActionPopup):
    """This form allows the user to create a new Shelf."""

    def create(self):
        self.add(
            npyscreen.TitleText,
            w_id="new_shelf_name",
            name="Add shelf: ",
            use_two_lines=False,
        )

    def on_cancel(self):
        self.get_widget("new_shelf_name").value = ""
        self.parentApp.setNextForm("MAIN")

    def on_ok(self):
        """When we hit okay, we check if the shelf name is blank. if not, adds a new Shelf to the library."""
        new_shelf_name = self.get_widget("new_shelf_name").value
        if new_shelf_name == "":
            self.notify_empty_shelf_name()
            return
        self.parentApp.library.add_shelf(new_shelf_name)
        self.get_widget("new_shelf_name").value = ""
        self.parentApp.setNextForm("MAIN")

    def notify_empty_shelf_name(self):
        message_to_print = "Shelf names must be one character or longer."
        npyscreen.notify_wait(message_to_print, title="Shelf Error")


class RenameShelfView(npyscreen.ActionPopup):
    def create(self):
        self.add(npyscreen.FixedText, value="Rename shelves below.")
        self.widget_ids = []

        # Create new widgets and keep track of their IDs
        for shelf in self.parentApp.library.contents:
            self.add(RenameEntryWidget, name=shelf.shelf_name, w_id=shelf.shelf_name)
            self.widget_ids.append(shelf.shelf_name)

    def on_ok(self):
        for widget_id in self.widget_ids:
            widget_handler = self.get_widget(widget_id)
            if widget_handler.has_been_edited == True:
                self.parentApp.library.rename_shelf(
                    widget_handler.name, widget_handler.value
                )
        self.parentApp.setNextForm("MAIN")


class RenameEntryWidget(npyscreen.TitleText):
    def __init__(
        self,
        screen,
        begin_entry_at=16,
        field_width=None,
        value=None,
        use_two_lines=None,
        hidden=False,
        labelColor="LABEL",
        allow_override_begin_entry_at=True,
        **keywords
    ):
        super().__init__(
            screen,
            begin_entry_at,
            field_width,
            value,
            use_two_lines,
            hidden,
            labelColor,
            allow_override_begin_entry_at,
            **keywords
        )

    def when_value_edited(self):
        self.has_been_edited = True
