import aspectlib

#Aspect
from aspect import check_if_user_exists, log

#Class
from services.manager import ResourceManager
from services.users import User

#Aspect Weaver
aspectlib.weave(ResourceManager, check_if_user_exists)
aspectlib.weave(ResourceManager, log)

user1 = User("toto", "xxx")
user1_ressource = ResourceManager(user1)
#jointPoint
user1_ressource.add("data")

user2 = User("not_exist", "xxx")
user2_ressource = ResourceManager(user2)
#jointPoint
user2_ressource.add("data")
