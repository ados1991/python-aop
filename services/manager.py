from services.resources import Resource


class ResourceManager:

    def __init__(self, user):
        self._user = user

    @property
    def username(self):
        return self._user.username

    def add(self, ressouce):
        Resource.add(ressouce)

    def delete(self, ressouce):
        Resource.delete(ressouce)

    def update(self, ressouce):
        Resource.update(ressouce)

    def get(self, ressouce):
        Resource.get(ressouce)
