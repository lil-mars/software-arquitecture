from ChickenBuilder import ChickenBuilder
class Kitchen:

    def __init__(self):
        self.__chicken_builder: ChickenBuilder = None

    def set_chicken_builder(self, chicken_builder):
        self.__chicken_builder = chicken_builder

    def get_chicken(self):
        return self.__chicken_builder.get_chicken()

    def build_chicken(self):
        self.__chicken_builder.create_chicken()
        self.__chicken_builder.build_flavor()
        self.__chicken_builder.build_ingredients()