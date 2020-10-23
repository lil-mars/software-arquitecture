from ICharge import ICharge

class FloorBoss(ICharge):
    def __init__(self, succesor: ICharge):
        self.succesor = succesor
        self.max_discount = 10
        

    def charge(self, quantity, unit_price):
        total_price = quantity * unit_price
        if (40 <= quantity and total_price < 18000) or  13000 <= total_price < 18000:
            return total_price - total_price * self.max_discount / 100
        else:
            print('Owner')
            return self.succesor.charge(quantity, unit_price)
         