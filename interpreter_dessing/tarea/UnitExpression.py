from Expression import Expression

class UnitExpression(Expression):
    def __init__(self, text):
        self.text = text

    def interpret(self):
        if self.text == 'cero':
            return self.zero()
        elif self.text == 'uno':
            return self.one()
        elif self.text == 'dos':
            return self.two()
        elif self.text == 'tres':
            return self.three()
        elif self.text == 'cuatro':
            return self.four()
        elif self.text == 'cinco':
            return self.five()
        elif self.text == 'seis':
            return self.six()
        elif self.text == 'siete':
            return self.seven()
        elif self.text == 'ocho':
            return self.eight()
        elif self.text == 'nueve':
            return self.nine()    

    def zero(self):
        return 0
    
    def one(self):
        return 1
    
    def two(self):
        return 2
    
    def three(self):
        return 3
    
    def four(self):
        return 4
    
    def five(self):
        return 5
    
    def six(self):
        return 6
    
    def seven(self):
        return 7
    
    def eight(self):
        return 8
    
    def nine(self):
        return 9

    def sum(self, num1, num2):
        return num1 + num2

    def substract(self, num1, num2):
        return num1 - num2