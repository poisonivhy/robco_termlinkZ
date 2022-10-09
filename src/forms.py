import npyscreen


class TermLinkInitForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleText, name="Welcome To Robco Industries (TM) Termlink", value="")

    def afterEditing(self):
        self.parentApp.setNextForm(None)
