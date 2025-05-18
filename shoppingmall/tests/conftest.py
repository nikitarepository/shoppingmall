# tests/conftest.py

import pytest
from app.domain.user import User
from app.domain.cart import Cart
from app.domain.product import Product
from pathlib import Path

@pytest.fixture
def authenticated_user():
    """로그인된 사용자"""
    user = User("tester")
    user.login("secret123")
    return user

@pytest.fixture
def cart(authenticated_user):
    """빈 장바구니 (사용자 포함)"""
    return Cart(authenticated_user)

@pytest.fixture
def sample_product():
    """예제용 상품"""
    return Product("Keyboard", 50000)

@pytest.fixture(scope="module")
def cart_with_log(tmp_path_factory):
    log_dir = tmp_path_factory.mktemp("log_dir")
    log_file = log_dir / "cart.log"

    user = User("loguser")
    user.login("secret123")
    cart = Cart(user)

    print(f"[SETUP] 로그파일 생성됨: {log_file}")
    log_file.write_text("[START] 장바구니 테스트 로그\n")

    yield cart

    log_file.write_text(log_file.read_text() + "[END] 테스트 종료\n")
    if log_file.exists():
        log_file.unlink()
        print("[TEARDOWN] 로그파일 삭제 완료")