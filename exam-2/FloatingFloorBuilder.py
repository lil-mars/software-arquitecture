from abc import ABC

from FloatingFloor import FloatingFloor
from Placement import Placement
from Price import Price
class FloatingFloorBuilder(ABC):
    def __init__(self, millimetre, placement, color):
        self.floor: FloatingFloor = None
        self.millimetre = millimetre
        self.placement = placement
        self.color = color
    
    def create_floor(self):
        pass

    def get_floor(self):
        return self.floor

    def build_thickness(self):
        pass

    def build_placement(self):
        placements = {
            'Colocacion flotante': 5,
            'Mecanismo clic': 6,
            'Fibra de vidrio': 7
        }
        self.floor.set_placement(Placement(self.placement, Price(placements[self.placement])))
    
    def build_color(self):
        self.floor.set_color(self.color)