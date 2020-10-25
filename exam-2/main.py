from App import App
from MelamineFloorBuilder import MelamineFloorBuilder
from OutsideFloorBuilder import OutsideFloorBuilder
from WoodFloorBuilder import WoodFloorBuilder

app = App()
floating_floors = ['Melaminico', 'Madera', 'Exterior']
placements = ['Colocacion flotante', 'Mecanismo clic', 'Fibra de vidrio']

while True:
    [print(index, floor) for index, floor in enumerate(floating_floors)]
    opt = input()

    print('Grosor en milimetros:')
    millimeters = float(input())
    [print(index, placement) for index, placement in enumerate(placements)]
    print('Tipo de colocacion:')
    placement = placements[int(input())]

    print('Color:')
    color = input()

    if opt == '0':
        builder = MelamineFloorBuilder(millimeters, placement, color)
    elif opt == '1':
        builder = WoodFloorBuilder(millimeters, placement, color)
    elif opt == '2':
        builder = OutsideFloorBuilder(millimeters, placement, color)
    app.set_floor_builder(builder)
    app.build_floor()
    floor = app.get_floor()
    print('Precio unidad', floor.calc_price())
    print('Ingresa metros cuadrados:')
    metters = int(input())
    price = metters * floor.calc_price()
    print('Precio',  price)

