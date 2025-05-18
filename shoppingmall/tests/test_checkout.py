# test_checkout.py

import pytest
from app.domain.product import Product
from app.domain.cart import Cart
from app.domain.user import User
from app.services.checkout_service import checkout

@pytest.fixture
def authenticated_user():
    user = User("checkout_user")
    user.login("secret123")
    return user

@pytest.fixture
def cart(authenticated_user):
    cart = Cart(authenticated_user)
    cart.add_product(Product("SSD", 120000))
    return cart

def test_checkout_success(cart):
    order = checkout(cart)
    assert order.status == "ORDERED"
    assert cart.items == []

def test_checkout_empty_cart(authenticated_user):
    cart = Cart(authenticated_user)
    with pytest.raises(ValueError):
        checkout(cart)

def test_checkout_unauthenticated_user():
    user = User("anonymous")
    cart = Cart(user)
    cart.add_product(Product("RAM", 80000))
    with pytest.raises(PermissionError):
        checkout(cart)
