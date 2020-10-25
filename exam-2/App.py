from FloatingFloorBuilder import FloatingFloorBuilder
class App:
    def __init__(self):
        self.builder: FloatingFloorBuilder = None
    
    def set_floor_builder(self, builder):
        self.builder = builder
    
    def get_floor(self):
        return self.builder.get_floor()
    
    def build_floor(self):
        self.builder.create_floor()
        self.builder.build_placement()
        self.builder.build_color()
        self.builder.build_thickness()


    