from enum import Enum


class ToppingsEnum(str, Enum):
    NONE = "NONE"
    SMOKED_HAM = "SMOKED_HAM"
    PEPPERONI = "PEPPERONI"
    KALAMATA_OLIVES = "KALAMATA_OLIVES"
    MUSHROOMS = "MUSHROOMS"
    JALAPENO = "JALAPENO"