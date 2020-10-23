from abc import ABC

class Sofa(ABC):
    def __init__(self):
        self.legs = 4

    def sit_on(self):
        return 'You are sitting on '
