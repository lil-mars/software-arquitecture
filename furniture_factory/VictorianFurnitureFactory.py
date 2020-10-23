from FurnitureFactory import FurnitureFactory
from VictorianChair import VictorianChair
from VictorianCoffeeTable import VictorianCoffeeTable
from VictorianSofa import VictorianSofa
class VictorianFurnitureFactory(FurnitureFactory):

    def __init__(self):
        pass

    def create_chair(self):
        return VictorianChair()

    def create_coffee_table(self):
        return VictorianCoffeeTable()

    def create_sofa(self):
        return VictorianSofa()