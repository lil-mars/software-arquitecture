from abc import ABC

class CoffeeTable(ABC):
    def __init__(self):
        self.legs = 4

    def put_on(self):
        return 'You are putting on something'