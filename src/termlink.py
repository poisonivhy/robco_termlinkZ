import npyscreen

import settings
from forms import TermLinkInitForm


class TermLink(npyscreen.NPSAppManaged):
    
    def onStart(self):
        self.registerForm("MAIN", TermLinkInitForm())


if __name__ == "__main__":
    term_link = TermLink()
    term_link.run()
