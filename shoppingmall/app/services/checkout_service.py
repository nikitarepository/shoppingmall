# app/services/checkout_service.py

from app.domain.cart import Cart
from app.domain.order import Order


def checkout(cart: Cart) -> Order:
    if not cart.items:
        raise ValueError("장바구니가 비어 있습니다.")
    if not cart.user.is_authenticated:
        raise PermissionError("로그인이 필요합니다.")

    order = Order(cart.items, cart.user)
    cart.clear()
    return order
