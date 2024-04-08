from typing import TYPE_CHECKING, List
from core.models.base import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func


class Analyzes(Base):
    __tablename__ = "analysis"

    analysis_id: Mapped[int]
    district_location_id: Mapped[str] = mapped_column(nullable=False)
    analysis_type: Mapped[str] = mapped_column(nullable=False)
    result: Mapped[str] = mapped_column(nullable=False)


class Forecast(Base):
    __tablename__ = "forecasts"

    forecast_id: Mapped[int]
    location: Mapped[str] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[str] = mapped_column(nullable=False)
