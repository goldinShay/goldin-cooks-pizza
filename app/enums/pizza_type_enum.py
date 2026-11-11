from enum import Enum


class PizzaTypeEnum(str, Enum):
    MARGHERITA = "MARGHERITA"
    CUSTOM = "CUSTOM"