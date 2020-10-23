from VictorianFurnitureFactory import VictorianFurnitureFactory
from ModernFurnitureFactory import ModernFurnitureFactory



victorian_factory = VictorianFurnitureFactory()
victorian_chair = victorian_factory.create_chair()
victorian_table = victorian_factory.create_coffee_table()
victorian_sofa = victorian_factory.create_sofa()
print(type(victorian_chair))
print(type(victorian_table))
print(type(victorian_sofa))
print(victorian_chair.sit_on())


modern_factory = ModernFurnitureFactory()
modern_chair = modern_factory.create_chair()
modern_sofa = modern_factory.create_sofa()
modern_coffee_table = modern_factory.create_coffee_table()

print(type(modern_coffee_table))
print(type(modern_chair))
print(type(modern_sofa))

