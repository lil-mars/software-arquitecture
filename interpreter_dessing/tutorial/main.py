from OrExpression import OrExpression 
from AndExpression import AndExpression
from TerminalExpression import TerminalExpression

def getMaleExpression():
    robert = TerminalExpression('Robert')
    jhon = TerminalExpression('Jhon')
    return OrExpression(robert, jhon)

def getMarriedWomanExpression():
    julie = TerminalExpression('Julie')
    married = TerminalExpression('Married')
    return AndExpression(julie, married)

def getSingleManExpression():
    pedro = TerminalExpression('Pedro')
    single = TerminalExpression('Single')
    return AndExpression(pedro, single)
def getFemaleExpression():
    martha = TerminalExpression('Martha')
    sarah = TerminalExpression('Sarah')
    return OrExpression(martha, sarah)

expr = getMaleExpression()
expr2 = getMarriedWomanExpression()
expr3 = getSingleManExpression()
expr4 = getFemaleExpression()

isMale = expr.interpret('Jhon')
isMarried = expr2.interpret('Married Julie')
isSingle = expr3.interpret('Pedro is Single')
isFemale = expr4.interpret('Jose')

print(f'Jhon is Male? {isMale}')
print(f'Julia is a married Woman? {isMarried}')
print(f'Is Pedro single? {isSingle}')
print(f'Is jose female? {isFemale}')
