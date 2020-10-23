from Expression import Expression

class SubstractExpression(Expression):
    def __init__(self):
        pass
    def set_values(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
        
    def interpret(self):
        return self.expr1 - self.expr2

