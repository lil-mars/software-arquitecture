from abc import ABC

class Chicken(ABC):
    def __init__(self ):
        self.__flavor = ''
        self.__ingredients = []
    
    def to_string(self):
        text = 'sabor de pollo: ' + self.__flavor + '\n' 
        text += 'Ingredientes: \n'
        for ing in self.__ingredients:
            text += ing + '\n'
        return text
    
    def add_ingredient(self, ingredient):
        self.__ingredients.append(ingredient)

    def set_flavor(self, flavor):
        self.__flavor = flavor

    def get_flavor(self):
        return self.__flavor