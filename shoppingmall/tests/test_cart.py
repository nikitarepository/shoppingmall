# tests/test_cart.py

from app.domain.cart import Cart
from app.domain.product import Product
from app.domain.user import User

def test_add_product():
    user = User("alice")
    cart = Cart(user)
    product = Product("Keyboard", 30000)

    cart.add_product(product)

    assert len(cart.items) == 1
    assert cart.items[0].name == "Keyboard"

def test_total_price():
    user = User("bob")
    cart = Cart(user)
    cart.add_product(Product("Mouse", 20000))
    cart.add_product(Product("Monitor", 150000))

    assert cart.total_price() == 170000
