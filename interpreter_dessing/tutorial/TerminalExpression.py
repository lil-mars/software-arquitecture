from IExpression import Expression
class TerminalExpression(Expression):

    def __init__(self, data):
        self.data = data
    
    def interpret(self, context):
        if context.count(self.data) > 0:
            return True
        return False