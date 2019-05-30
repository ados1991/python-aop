import aspectlib

from aspect.aspect import checks_user, log
from services.manager import ResourceManager
from services.users import User

aspectlib.weave(ResourceManager, checks_user)
aspectlib.weave(ResourceManager, log)

user1 = User("toto", "xxx")
user1_ressource = ResourceManager(user1)
user1_ressource.add("data")

user2 = User("not_exist", "xxx")
user2_ressource = ResourceManager(user2)
user2_ressource.add("data")
