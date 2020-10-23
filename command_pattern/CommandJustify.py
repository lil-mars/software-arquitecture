from ICommand import ICommand
class CommandJustify(ICommand):
    def __init__(self, text):
        self.text = text


    def run(self):
        self.text.justify()
    