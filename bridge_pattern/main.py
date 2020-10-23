from Bike import Bike
from Car import Car
from Produce import Produce
from Assemble import Assemble

car = Car(Produce(), Assemble())
car.manufacture()

bike = Bike(Produce(), Assemble())
bike.manufacture()