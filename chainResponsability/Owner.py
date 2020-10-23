from ICharge import ICharge

class Owner(ICharge):
    def __init__(self):
        self.discount = 15        

    def charge(self, quantity, unit_price):
        total_price = quantity * unit_price
        float(total_price)
        if quantity > 60 and  total_price >= 18000:
            return total_price - (total_price * self.discount) / 100
        else:
            print('No more')