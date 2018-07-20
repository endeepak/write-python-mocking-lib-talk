from mock import Mock
from order_service import OrderService, Order

def test_place_order_creates_order_in_repository():
    order_repository = Mock()
    order_service = OrderService(order_repository)
    order = Order(product='Python Programming Book', price=300)

    order_service.place_order(order)

    order_repository.create_order.assert_called_once_with(order)
