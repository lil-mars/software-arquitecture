from ChickenBuilder import ChickenBuilder

class SweetSourChickenBuilder(ChickenBuilder):
    def __init__(self):
        super().__init__()


    def build_ingredients(self):
        self._chicken.add_ingredient('vinagre')
        self._chicken.add_ingredient('maizena')
        self._chicken.add_ingredient('ketchup')
        self._chicken.add_ingredient('agua')

    def build_flavor(self):
        self._chicken.set_flavor('Agridulce')



