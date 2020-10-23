from IExpression import Expression

class AndExpression(Expression):
    def __init__(self,  expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def interpret(self, context):
        return self.expr1.interpret(context) and self.expr2.interpret(context)
