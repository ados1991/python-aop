
class User:

    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username
