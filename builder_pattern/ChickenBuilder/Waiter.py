from  Kitchen import Kitchen
class Waiter:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    
    def get_chicken(self, kitchen: Kitchen):
        return kitchen.get_chicken()

    