import logging
import aspectlib

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

USERS = [
    "toto", "tata"
]


@aspectlib.Aspect
def check_if_user_exists(self, *args, **kwargs):
    if self.username not in USERS:
        raise Exception(f"user {self.username} does not exist")
    result = yield aspectlib.Proceed
    yield aspectlib.Return(result)

@aspectlib.Aspect(bind=True)
def log(cutpoint, *args, **kwargs):
    logging.info(f"{cutpoint.__name__} got called with args: {args} kwargs: {kwargs}")
    result = yield aspectlib.Proceed
    logging.info(f"called func {cutpoint.__name__} returns result: {result}")
    yield aspectlib.Return(result)
