from FloatingFloorBuilder import FloatingFloorBuilder
from OutsideFloor import OutsideFloor
from Price import Price
from Thickness import Thickness

class OutsideFloorBuilder(FloatingFloorBuilder):

    def __init__(self,millimetre, placement, color):
        super().__init__(millimetre, placement, color)

    def create_floor(self):
        self.floor = OutsideFloor()

    def build_thickness(self):
        thickness = Thickness(self.millimetre, Price(5))
        self.floor.set_thickness(thickness)
