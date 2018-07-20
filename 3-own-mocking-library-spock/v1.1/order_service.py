class OrderService(object):
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def place_order(self, order):
        self.order_repository.create_order(order)


class Order(object):
    def __init__(self, product, price):
        self.product = product
        self.price = price


class OrderRepository(object):
    def __init__(self, database):
        self.database = database

    def create_order(self, order):
        self.database.save(order)
