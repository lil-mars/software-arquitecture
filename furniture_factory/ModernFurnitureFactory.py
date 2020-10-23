from FurnitureFactory import FurnitureFactory
from ModernChair import ModernChair
from ModernCoffeeTable import ModerCoffeeTable
from ModernSofa import ModernSofa

class ModernFurnitureFactory(FurnitureFactory):
    def __init__(self):
        pass

    def create_chair(self):
        return ModernChair()

    def create_coffee_table(self):
        return ModerCoffeeTable()

    def create_sofa(self):
        return ModernSofa()