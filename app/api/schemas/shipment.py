# from enum import Enum
# from pydantic import BaseModel, Field


# class ShipmentStatus(str, Enum):
#     placed = "placed"
#     in_transit = "in_transit"
#     out_for_delivery = "out_for_delivery"
#     delivered = "delivered"


# class BaseShipment(BaseModel):
#     content: str
#     weight: float = Field(le=25)
#     destination: int


# class ShipmentRead(BaseShipment):
#     status: ShipmentStatus


# class ShipmentCreate(BaseShipment):
#     pass
    

# class ShipmentUpdate(BaseModel):
#     content: str | None = Field(default=None)
#     weight: float | None = Field(default=None, le=25)
#     destination: int | None = Field(default=None)
#     status: ShipmentStatus

# schemas.py
# from enum import Enum
# from pydantic import BaseModel, Field
# from typing import Optional


# class ShipmentStatus(str, Enum):
#     placed = "placed"
#     in_transit = "in_transit"
#     out_for_delivery = "out_for_delivery"
#     delivered = "delivered"


# class BaseShipment(BaseModel):
#     content: str
#     weight: float = Field(le=25, description="Weight must be <= 25")
#     destination: int


# class ShipmentRead(BaseShipment):
#     id: int  # Add ID field for read operations
#     status: ShipmentStatus


# class ShipmentCreate(BaseShipment):
#     pass
    

# class ShipmentUpdate(BaseModel):
#     content: Optional[str] = None
#     weight: Optional[float] = Field(default=None, le=25, description="Weight must be <= 25")
#     destination: Optional[int] = None
#     status: Optional[ShipmentStatus] = None  # Make status optional for PATCH

from datetime import datetime
from pydantic import BaseModel, Field

from app.database.models import ShipmentStatus


class BaseShipment(BaseModel):
    content: str
    weight: float = Field(le=25)
    destination: int


class ShipmentRead(BaseShipment):
    id: int
    status: ShipmentStatus
    estimated_delivery: datetime


class ShipmentCreate(BaseShipment):
    pass
    

class ShipmentUpdate(BaseModel):
    status: ShipmentStatus | None = Field(default=None)
    estimated_delivery: datetime | None = Field(default=None)