from Seller import Seller
from FloorBoss import FloorBoss
from Owner import Owner
owner = Owner()
boss = FloorBoss(owner)
seller = Seller(boss)

while True:
    quantity = int(input())
    price = int(input())
    print(seller.charge(quantity, price))