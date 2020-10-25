from FloatingFloor import FloatingFloor
from Price import Price

class OutsideFloor(FloatingFloor):
    def __init__(self):
        super().__init__()
        self.price = Price(15)
