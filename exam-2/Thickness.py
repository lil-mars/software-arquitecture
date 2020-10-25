from Price import Price

class Thickness:
    def __init__(self, millimeters, price):
        self.millimeters = millimeters
        self.price: Price = price
    
    def calc_price(self):
        return self.millimeters * self.price.get_value()
