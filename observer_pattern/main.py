from Order import Order
from Kitchen import Kitchen

order = Order('Jose Jimenez')
order2 = Order('Carlos Mesa')

kitchen = Kitchen()

kitchen.attach(order)
kitchen.attach(order2)

kitchen.prepare_orders()
kitchen.show_orders()