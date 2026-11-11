import uuid

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base
from app.enums.order_status_enum import OrderStatEnum
from app.enums.payment_status_enum import PaymentStatusEnum
from app.enums.pizza_type_enum import PizzaTypeEnum
from app.enums.toppings_enum import ToppingsEnum


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # Human-friendly number shown to customer/worker, e.g. "P-20261111-0042"
    order_number = Column(
        String(30),
        unique=True,
        nullable=False
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )

    status = Column(
        Enum(OrderStatEnum),
        nullable=False,
        default=OrderStatEnum.RECEIVED,
        index=True
    )

    pickup_time = Column(
        DateTime(timezone=True),
        nullable=True
    )

    total_amount = Column(
        Numeric(10, 2),
        nullable=False,
        default=0
    )

    # --- Payment (provider-agnostic: Mollie / Adyen / Stripe) ---
    payment_status = Column(
        Enum(PaymentStatusEnum),
        nullable=False,
        default=PaymentStatusEnum.UNPAID,
        index=True
    )

    payment_provider = Column(
        String(20),
        nullable=True
    )

    # The provider's own ID (Mollie tr_..., Stripe pi_..., Adyen pspReference)
    payment_reference = Column(
        String(255),
        unique=True,
        nullable=True
    )

    notes = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship("User", back_populates="orders")

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    order_id = Column(
        UUID(as_uuid=True),
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    pizza_type = Column(
        Enum(PizzaTypeEnum),
        nullable=False,
        default=PizzaTypeEnum.MARGHERITA
    )

    topping_1 = Column(
        Enum(ToppingsEnum),
        nullable=False,
        default=ToppingsEnum.NONE
    )

    topping_2 = Column(
        Enum(ToppingsEnum),
        nullable=False,
        default=ToppingsEnum.NONE
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=1
    )

    # Price at time of ordering, so later price changes don't alter history
    unit_price = Column(
        Numeric(10, 2),
        nullable=False
    )

    order = relationship("Order", back_populates="items")