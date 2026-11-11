from enum import Enum


class OrderStatEnum(str, Enum):
    RECEIVED = "RECEIVED"
    IN_PROGRESS = "IN_PROGRESS"
    READY = "READY"
    CLOSED = "CLOSED"