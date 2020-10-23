from ChickenBuilder import ChickenBuilder

class BarbecueChickenBuilder(ChickenBuilder):
    def __init__(self):
        super().__init__()
    
    def build_ingredients(self):
        self._chicken.add_ingredient('Harina')
        self._chicken.add_ingredient('huevos')
        self._chicken.add_ingredient('pan rallado')
        self._chicken.add_ingredient('ajo en polvo')

    def build_flavor(self):
        self._chicken.set_flavor('barbacoa')