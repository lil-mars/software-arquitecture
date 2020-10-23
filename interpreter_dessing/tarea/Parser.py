from SumExpression import SumExpression
from SubstractExpression import SubstractExpression
from UnitExpression import UnitExpression

class Parser:
    def __init__(self, text):
        self.result = 0
        self.items = []
        self.parse(text)

    def parse(self, text):
        for part in text.split(' '):
            if part == 'mas':
                self.items.append(SumExpression())
            elif part == 'menos':
                self.items.append(SubstractExpression())
            else:
                self.items.append(UnitExpression(part))
                print(part)
        self.calculate()

    def calculate(self):
        for index in range(1,len(self.items),2):
            if self.result != 0:
                self.items[index].set_values(self.result, self.items[index+1].interpret())
                self.result = self.items[index].interpret()
            else:
                self.items[index].set_values(self.items[index-1].interpret(), self.items[index+1].interpret())
                self.result = self.items[index].interpret()
                
    def get_result(self):
        return self.result