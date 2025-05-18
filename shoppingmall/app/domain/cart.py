# app/domain/cart.py

from app.domain.product import Product
from app.domain.user import User


class Cart:
    def __init__(self, user: User):
        self.user = user
        self.items: list[Product] = []

    def add_product(self, product: Product):
        self.items.append(product)

    def total_price(self) -> int:
        return sum(item.price for item in self.items)

    def clear(self):
        self.items = []
