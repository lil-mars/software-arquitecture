from ICommand import ICommand
class CommandRemoveBold(ICommand):
    def __init__(self, text):
        self.text = text

    def run(self):
        self.text.remove_bold()
    