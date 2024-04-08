from datetime import date, datetime
from typing import Annotated, List
import uuid
from pydantic import BaseModel, ConfigDict


class DistrictsInfoBase(BaseModel):
    district_name: str
    district_category: str


class RouteInfoBase(BaseModel):
    start_point: str
    end_point: str
    creation_time: date
    update_time: date
    base_point: str
    district_number: int


class RouteInfoRouteid:
    def __init__(self, route_id: int = None):
        self.route_id = route_id


class RouteInfoSensorid:
    def __init__(self, sensor_id: int = None):
        self.sensor_id = sensor_id


class RouteInfo(RouteInfoBase):
    model_config = ConfigDict(from_attributes=True)
    route_number: int


class RouteInfoUpdate(RouteInfoBase):
    model_config = ConfigDict(from_attributes=True)


class DistrictsInfo(DistrictsInfoBase):
    model_config = ConfigDict(from_attributes=True)
    district_number: int


class DistrictsInfoCreate(DistrictsInfoBase):
    model_config = ConfigDict(from_attributes=True)
    district_number: int


class DistrictsInfoUpdate(DistrictsInfoBase):
    model_config = ConfigDict(from_attributes=True)
    # id: uuid.UUID
