from abc import ABC
from src.facades.env import Env
from redis_om import get_redis_connection

redis = get_redis_connection(url=f"redis://{Env().db.host}:{Env().db.port}/0")


class BaseRedisMetaClass(ABC):
    global_key_prefix = Env().project_name
    database = redis
