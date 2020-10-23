from CommandChangeColor import CommandChangeColor
from CommandJustify import CommandJustify
from CommandMakeBold import CommandMakeBold

from CommandRemoveBold import CommandRemoveBold
from CommandRemoveColor import CommandRemoveColor
from CommandRemoveJustify import CommandRemoveJustify

class TextControl:

    def __init__(self, text):
        self.__commands = []
        self.__commands.append(CommandChangeColor(text, 'Rojo'))
        self.__commands.append(CommandJustify(text))
        self.__commands.append(CommandMakeBold(text))
        
        self.__commands.append(CommandRemoveBold(text))
        self.__commands.append(CommandRemoveColor(text))
        self.__commands.append(CommandRemoveJustify(text))
        

    def get_commands(self):
        return self.__commands
        
    def press_command(self, number):
        self.__commands[number].run()