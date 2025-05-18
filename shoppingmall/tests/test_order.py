# test_order.py

import pytest
from app.domain.order import Order
from app.domain.product import Product
from app.domain.user import User

@pytest.fixture
def authenticated_user():
    user = User("buyer")
    user.login("secret123")
    return user

def test_order_creation(authenticated_user):
    items = [Product("Phone", 1000000)]
    order = Order(items, authenticated_user)
    assert order.status == "ORDERED"

def test_order_total_price(authenticated_user):
    items = [Product("A", 1000), Product("B", 2000)]
    order = Order(items, authenticated_user)
    assert order.total_price() == 3000

def test_order_mark_paid(authenticated_user):
    order = Order([Product("C", 100)], authenticated_user)
    order.mark_paid()
    assert order.status == "PAID"

def test_order_mark_shipped(authenticated_user):
    order = Order([Product("D", 500)], authenticated_user)
    order.mark_shipped()
    assert order.status == "SHIPPED"
