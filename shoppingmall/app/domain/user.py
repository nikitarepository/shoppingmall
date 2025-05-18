# app/domain/user.py

class User:
    def __init__(self, username: str, authenticated: bool = False):
        self.username = username
        self._authenticated = authenticated

    @property
    def is_authenticated(self) -> bool:
        return self._authenticated

    def login(self, password: str):
        if password == "secret123":
            self._authenticated = True

    def logout(self):
        self._authenticated = False
