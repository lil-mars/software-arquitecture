from abc import ABC, abstractmethod

class Chair(ABC):
    def __init__(self):
        self.legs = 4
    
    def sit_on(self):
        return 'You are sitting on.'

