from Height import Height
from Width import Width
from abc import ABC

class FloatingFloor(ABC):
    def __init__(self):
        self.__thickness = None
        self.__placement = None
        self.__height = Height(30.0)
        self.__width = Width(120.0)
        self.__color = None

    def set_thickness(self, thickness):
        self.__thickness =  thickness
    def set_placement(self, placement):
        self.__placement =  placement
    def set_color(self, color):
        self.__color = color

