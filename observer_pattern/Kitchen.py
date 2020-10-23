from Subject import Subject
from random import randrange


class Kitchen(Subject):
    def __init__(self):
        self.__orders = []

    def detach(self, order):
        self.__orders.remove(order)

    def attach(self, order):
        self.__orders.append(order)

    def notify(self):
        print('Notificar ordenes')
        for order in self.__orders:
            order.update(1)

    def prepare_orders(self):
        print('Preparando ordenes!')
        for order in self.__orders:
            order.quality = randrange(10)
        print('Listo!')
        self.notify()

    def show_orders(self):
        for order in self.__orders:
            print(f'Cliente: {order.client}\nCalidad de la orden:{order.quality}\nEstado:{order.state}')