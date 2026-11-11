import uuid
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from app.enums.order_status_enum import OrderStatEnum
from app.enums.payment_status_enum import PaymentStatusEnum
from app.enums.pizza_type_enum import PizzaTypeEnum
from app.enums.toppings_enum import ToppingsEnum


# ---------- What the customer SENDS ----------

class OrderItemCreate(BaseModel):
    pizza_type: PizzaTypeEnum
    topping_1: ToppingsEnum = ToppingsEnum.NONE
    topping_2: ToppingsEnum = ToppingsEnum.NONE
    quantity: int = Field(default=1, ge=1, le=10)


class OrderCreate(BaseModel):
    items: List[OrderItemCreate] = Field(min_length=1, max_length=20)
    pickup_time: Optional[datetime] = None
    notes: Optional[str] = Field(default=None, max_length=500)


# ---------- What a worker SENDS ----------

class OrderStatusUpdate(BaseModel):
    status: OrderStatEnum


# ---------- What the API SENDS BACK ----------

class OrderItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    pizza_type: PizzaTypeEnum
    topping_1: ToppingsEnum
    topping_2: ToppingsEnum
    quantity: int
    unit_price: Decimal


class OrderRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    order_number: str
    status: OrderStatEnum
    payment_status: PaymentStatusEnum
    pickup_time: Optional[datetime] = None
    total_amount: Decimal
    notes: Optional[str] = None
    created_at: datetime
    items: List[OrderItemRead]