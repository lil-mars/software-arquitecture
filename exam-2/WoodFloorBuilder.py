from FloatingFloorBuilder import FloatingFloorBuilder
from WoodFloor import WoodFloor
from Price import Price
from Thickness import Thickness

class WoodFloorBuilder(FloatingFloorBuilder):

    def __init__(self,millimetre, placement, color):
        super().__init__(millimetre, placement, color)

    def create_floor(self):
        self.floor = WoodFloor()

    def build_thickness(self):
        thickness = Thickness(self.millimetre, Price(15))
        self.floor.set_thickness(thickness)
