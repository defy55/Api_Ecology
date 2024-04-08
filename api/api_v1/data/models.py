from datetime import datetime
from core.models.base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column


class SensorData(Base):
    __tablename__ = "sensor_data"

    data_id: Mapped[int]
    data_type: Mapped[str] = mapped_column(nullable=False)
    value: Mapped[float] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False)
    district_id: Mapped[int] = mapped_column(nullable=False)
    route_id: Mapped[int] = mapped_column(nullable=False)
    sensor_id: Mapped[int] = mapped_column(nullable=False)
    sensor_type: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=True)
