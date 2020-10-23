from Waiter import Waiter
from Kitchen import Kitchen
from BarbecueChickenBuilder import BarbecueChickenBuilder
from SweetSourChickenBuilder import SweetSourChickenBuilder
from MustardChickenBuilder import MustardChickenBuilder

waiter = Waiter('Erick', 'Terrazas')
barbecue_builder = BarbecueChickenBuilder()
sweet_sour_builder = SweetSourChickenBuilder()
mustard_builder = MustardChickenBuilder()



kitchen = Kitchen()

kitchen.set_chicken_builder(barbecue_builder)
kitchen.build_chicken()
barbecue_chicken = waiter.get_chicken(kitchen)
print(barbecue_chicken.to_string())

kitchen.set_chicken_builder(sweet_sour_builder)
kitchen.build_chicken()
sweet_sour_chicken = waiter.get_chicken(kitchen)
print(sweet_sour_chicken.to_string())

kitchen.set_chicken_builder(mustard_builder)
kitchen.build_chicken()
mustard_chicken = waiter.get_chicken(kitchen)
print(mustard_chicken.to_string())
