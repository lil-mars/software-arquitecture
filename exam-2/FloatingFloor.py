from Height import Height
from Width import Width
from Thickness import Thickness
from abc import ABC
from Price import Price
from Placement import Placement
class FloatingFloor(ABC):
    def __init__(self):
        self.thickness: Thickness = None
        self.placement: Placement = None
        self.height = Height(30.0)
        self.width = Width(120.0)
        self.color = None
        self.price: Price = None

    def get_thickness(self):
        return self.thickness

    def get_placement(self):
        return self.placement

    def set_thickness(self, thickness):
        self.thickness = thickness

    def set_placement(self, placement):
        self.placement =  placement
        
    def set_color(self, color):
        self.color = color
    
    def calc_price(self):
        price = 0
        price += self.price.get_value()
        price += self.thickness.calc_price()
        price += self.placement.price.get_value()
        return price