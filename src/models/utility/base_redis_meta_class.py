from abc import ABC
from src.facades.env import Env


class BaseRedisMetaClass(ABC):
    global_key_prefix = Env().project_name
