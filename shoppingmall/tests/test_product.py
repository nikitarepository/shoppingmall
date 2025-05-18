# test_product.py

from app.domain.product import Product

def test_product_attributes():
    product = Product("Tablet", 200000)
    assert product.name == "Tablet"
    assert product.price == 200000
