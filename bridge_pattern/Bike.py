from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, workshop, workshop2):
        super().__init__(workshop, workshop2)
    
    def manufacture(self):
        print('Bike')
        self.produce_workshop.work()
        self.assemble_workshop.work()