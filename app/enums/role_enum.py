from enum import Enum


class RoleEnum(str, Enum):
    USER = "USER"
    WORKER = "WORKER"
    ADMIN = "ADMIN"