from FloatingFloorBuilder import FloatingFloorBuilder
from MelamineFloor import MelamineFloor
from Price import Price
from Thickness import Thickness

class MelamineFloorBuilder(FloatingFloorBuilder):

    def __init__(self):
        super().__init__()

    def create_floor(self):
        self.floor = MelamineFloor()

    def build_thickness(self, millimeters):
        thickness = Thickness()
        self.floor.set_thickness(millimeters, Price(5))
    def build_placement(self, placement):
        self.floor.set_placement()
