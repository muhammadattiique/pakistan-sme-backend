from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


# ----------------------------
# Base Schema
# ----------------------------

class BusinessBase(BaseModel):
    name: str
    industry: str
    city: str

    address: Optional[str] = None

    website: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    whatsapp: Optional[str] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    source: str = "OpenStreetMap"


# ----------------------------
# Create Schema
# ----------------------------

class BusinessCreate(BusinessBase):
    osm_id: str


# ----------------------------
# Update Schema
# ----------------------------

class BusinessUpdate(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    city: Optional[str] = None

    address: Optional[str] = None

    website: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    whatsapp: Optional[str] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    source: Optional[str] = None


# ----------------------------
# Response Schema
# ----------------------------

class Business(BusinessBase):
    id: int
    osm_id: str

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )