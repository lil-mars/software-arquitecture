from Parser import Parser

expression = 'uno mas cinco mas dos menos tres'
parser = Parser(expression)
print(parser.get_result())