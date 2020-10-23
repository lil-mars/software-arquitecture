from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, workshop, workshop2):
        super().__init__(workshop, workshop2)

    def manufacture(self):
        print('Auto')
        self.produce_workshop.work()
        self.assemble_workshop.work()