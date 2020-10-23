from ICharge import ICharge

class Seller(ICharge):
    def __init__(self, succesor: ICharge):
        self.succesor = succesor
        self.max_discount =  5
        self.min_discount = 1.5

    def charge(self, quantity, unit_price):
        total_price = quantity * unit_price
        if 8 <= quantity < 20:
            return float(total_price) - float(total_price) * self.min_discount / 100.0
        elif 20 <= quantity < 40 and 8000 < total_price < 13000:
            return total_price - total_price * self.max_discount / 100
        elif quantity < 8:
            return total_price
        else:
            print('Floor Boss')
            return self.succesor.charge(quantity, unit_price)
         
