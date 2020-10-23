from Observer import Observer

class Order(Observer):
    def __init__(self, client):
        self.client = client
        self.state = 0
        self.quality = None

    def update(self, state):
        self.state = state