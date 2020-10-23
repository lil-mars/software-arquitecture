from Expression import Expression
class SumExpression(Expression):
    def __init__(self):
        self.expr1 = None
        self.expr2 = None
        pass
    def set_values(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
    def interpret(self):
        return self.expr1 + self.expr2

