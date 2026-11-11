import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.enums.role_enum import RoleEnum


class UserRead(BaseModel):
    """What the API sends back about a user."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    customer_number: str
    role: RoleEnum
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    username: Optional[str] = None
    email: str
    phone_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    street: Optional[str] = None
    house_number: Optional[str] = None
    house_number_suffix: Optional[str] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None


class UserUpdate(BaseModel):
    """What a user may change about their own profile.

    Not included on purpose: role, email, google_id, customer_number.
    """

    first_name: Optional[str] = Field(default=None, max_length=100)
    middle_name: Optional[str] = Field(default=None, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    username: Optional[str] = Field(default=None, max_length=100)
    phone_number: Optional[str] = Field(default=None, max_length=50)
    date_of_birth: Optional[date] = None
    street: Optional[str] = Field(default=None, max_length=255)
    house_number: Optional[str] = Field(default=None, max_length=20)
    house_number_suffix: Optional[str] = Field(default=None, max_length=20)
    postal_code: Optional[str] = Field(default=None, max_length=20)
    city: Optional[str] = Field(default=None, max_length=100)