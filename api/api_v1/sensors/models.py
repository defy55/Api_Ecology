from datetime import datetime
from core.models.base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


class StationarySensor(Base):
    __tablename__ = "stationary_sensors"

    sensor_id: Mapped[int]
    power_source: Mapped[str] = mapped_column(String(20), nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=True)
    last_update: Mapped[datetime] = mapped_column(nullable=True)
    location: Mapped[str] = mapped_column(nullable=True)
    error_status: Mapped[str] = mapped_column(nullable=True)
    activity_time: Mapped[int] = mapped_column(nullable=True)


class MobileSensor(Base):
    __tablename__ = "mobile_sensors"

    sensor_id = Mapped[int]
    power_source: Mapped[str] = mapped_column(String(20), nullable=False)
    battery_level: Mapped[float] = mapped_column(nullable=False)
    current_location = Mapped[str]
    is_active: Mapped[bool] = mapped_column(nullable=True)
    last_update: Mapped[datetime]
    sensor_id: Mapped[int]
    location: Mapped[str]
    error_status: Mapped[str]
    activity_time: Mapped[str]
