# app/domain/order.py

import uuid
from app.domain.product import Product
from app.domain.user import User


class Order:
    def __init__(self, items: list[Product], user: User):
        if not items:
            raise ValueError("빈 주문은 생성할 수 없습니다.")
        if not user.is_authenticated:
            raise PermissionError("로그인된 사용자만 주문할 수 있습니다.")

        self.id = str(uuid.uuid4())
        self.items = items
        self.user = user
        self.status = "ORDERED"

    def total_price(self) -> int:
        return sum(item.price for item in self.items)

    def mark_paid(self):
        self.status = "PAID"

    def mark_shipped(self):
        self.status = "SHIPPED"
