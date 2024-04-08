from datetime import datetime
from core.models.base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func


class District(Base):
    __tablename__ = "districts"

    district_number: Mapped[int]
    district_name: Mapped[str] = mapped_column(nullable=False)
    district_category: Mapped[str] = mapped_column(nullable=False)


class Route(Base):
    __tablename__ = "routes"

    route_number: Mapped[int]
    start_point: Mapped[str] = mapped_column(nullable=False)
    end_point: Mapped[str] = mapped_column(nullable=False)
    creation_time: Mapped[datetime] = mapped_column(nullable=False)
    update_time: Mapped[datetime] = mapped_column(nullable=False)
    base_point: Mapped[str] = mapped_column(nullable=False)
    district_number: Mapped[int]
