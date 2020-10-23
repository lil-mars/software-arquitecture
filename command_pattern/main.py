from TextControl import TextControl
from Text import Text

text = Text('Esta es una prueba de texto')
control = TextControl(text)

for command in control.get_commands():
    command.run()