

class Resource:

    @classmethod
    def add(cls, resource):
        print(f"add {resource}")

    @classmethod
    def update(cls, resource):
        print(f"update {resource}")

    @classmethod
    def get(cls, resource):
        print(f"get {resource}")

    @classmethod
    def delete(cls, resource):
        print(f"delete {resource}")
