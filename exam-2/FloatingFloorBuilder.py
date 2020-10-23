from abc import ABC
from FloatingFloor import FloatingFloor
class FloatingFloorBuilder(ABC):
    def __init__(self):
        self.floor = None
    
    def create_floor(self):
        self.floor = FloatingFloor()

    def get_floor(self):
        return self.floor

    def build_thickness(self, milimeters):
        pass

    def build_placement(self, placement):
        pass
    
    def build_color(self, color):
        pass