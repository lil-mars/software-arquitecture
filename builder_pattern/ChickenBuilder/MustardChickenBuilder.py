from ChickenBuilder import ChickenBuilder

class MustardChickenBuilder(ChickenBuilder):
    def __init__(self):
        super().__init__()
    
    def build_ingredients(self):
        self._chicken.add_ingredient('Harina')
        self._chicken.add_ingredient('mostaza')
        self._chicken.add_ingredient('crema de leche')
        self._chicken.add_ingredient('pimienta')
        self._chicken.add_ingredient('cebollin')
        

    def build_flavor(self):
        self._chicken.set_flavor('mostaza')