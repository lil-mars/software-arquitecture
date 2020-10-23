from ICommand import ICommand
class CommandRemoveColor(ICommand):
    def __init__(self, text):
        self.text = text

    def run(self):
        self.text.change_color('black')
    