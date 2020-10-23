from ICommand import ICommand
class CommandChangeColor(ICommand):
    def __init__(self, text, color):
        self.text = text
        self.color = color


    def run(self):
        self.text.change_color(self.color)
    