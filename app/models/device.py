from uuid import uuid4, UUID
from datetime import datetime

from sqlalchemy import Column, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as UUIDColumn
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from models.user import User
from database import Base, session


class Device(Base):
    __tablename__ = "devices"

    uuid = Column(UUIDColumn(as_uuid=True), primary_key=True, index=True, default=uuid4)
    latitude = Column(Float, nullable=False, default=0)
    longitude = Column(Float, nullable=False, default=0)

    user_uuid = Column(UUIDColumn(as_uuid=True), ForeignKey("user.uuid", ondelete="CASCADE"))

    user = relationship("User", back_populates="devices", passive_deletes=True)


class DeviceDelete(BaseModel):
    device_uuid: UUID


class DeviceUpdatePosition(BaseModel):
    device_uuid: UUID
    lat: float
    lon: float


class DevicesList(BaseModel):
    devices: list[UUID]


class DeviceUpdateCoordinates(BaseModel):
    device: UUID
    latitude: float
    longitude: float
