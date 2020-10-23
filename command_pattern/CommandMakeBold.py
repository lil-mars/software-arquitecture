from ICommand import ICommand
class CommandMakeBold(ICommand):
    def __init__(self, text):
        self.text = text

    def run(self):
        self.text.make_bold()
    