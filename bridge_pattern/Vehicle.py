from abc import ABC

class Vehicle(ABC):
    def __init__(self, workshop, workshop2):
        self.produce_workshop =  workshop
        self.assemble_workshop = workshop2

    def manufacture(self):
        pass