# test_user.py

from app.domain.user import User

def test_login_success():
    user = User("tester")
    user.login("secret123")
    assert user.is_authenticated

def test_login_failure():
    user = User("tester")
    user.login("wrongpass")
    assert not user.is_authenticated

def test_logout():
    user = User("tester")
    user.login("secret123")
    user.logout()
    assert not user.is_authenticated
