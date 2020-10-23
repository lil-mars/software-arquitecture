from abc import ABC
from Chicken import Chicken

class ChickenBuilder(ABC):
    def __init__(self):
        self._chicken:Chicken = None
    
    def create_chicken(self):
        self._chicken = Chicken()

    def get_chicken(self):
        return self._chicken

    def build_ingredients(self):
        pass

    def build_flavor(self):
        pass
    

