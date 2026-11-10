import uuid

from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base
from app.enums.role_enum import RoleEnum


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    customer_number = Column(
        String(20),
        unique=True,
        nullable=False
    )

    google_id = Column(
        String(255),
        unique=True,
        nullable=True
    )

    role = Column(
        Enum(RoleEnum),
        nullable=False,
        default=RoleEnum.USER
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    middle_name = Column(
        String(100),
        nullable=True
    )

    last_name = Column(
        String(100),
        nullable=False
    )

    username = Column(
        String(100),
        unique=True,
        nullable=True
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    phone_number = Column(
        String(50),
        nullable=True
    )

    date_of_birth = Column(
        Date,
        nullable=True
    )

    street = Column(
        String(255),
        nullable=True
    )

    house_number = Column(
        String(20),
        nullable=True
    )

    house_number_suffix = Column(
        String(20),
        nullable=True
    )

    postal_code = Column(
        String(20),
        nullable=True
    )

    city = Column(
        String(100),
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