from fastapi import Query
from pydantic import BaseModel, ConfigDict


class ForecastBase(BaseModel):
    forecast_id: int
    location: str
    category: str
    rating: int | None = Query(None, ge=1, le=10)


class AnalysisBase(BaseModel):
    analysis_id: int
    district_locationid: str
    analysis_type: str
    result: str


class SForecast(ForecastBase):
    model_config = ConfigDict(from_attributes=True)


class SAnalysis(AnalysisBase):
    model_config = ConfigDict(from_attributes=True)


class AnalysisQ:
    def __init__(
        self, analysis_id: int, location: str, analysis_type: str, result: str
    ):
        self.analysis_id = analysis_id
        self.location = location
        self.analysis_type = analysis_type
        self.result = result
