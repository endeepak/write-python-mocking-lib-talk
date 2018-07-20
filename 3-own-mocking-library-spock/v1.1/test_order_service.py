from spock import Spock
from order_service import OrderService, Order


def test_place_order_creates_order_in_repository():
    order_repository = Spock()
    order_service = OrderService(order_repository)
    order = Order(product='Python Programming Book', price=300)

    order_service.place_order(order)

    assert order_repository.create_order.was_called_with(order)
