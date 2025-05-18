# app/domain/product.py

class Product:
    """
    상품을 나타내는 클래스입니다.

    >>> p = Product("Keyboard", 50000)
    >>> p.name
    'Keyboard'
    >>> p.price
    50000
    """
    
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
