from typing import Annotated
from datetime import date
from xmlrpc.client import Boolean
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict


class SensorDataBase(BaseModel):
    data_type: Annotated[str, MinLen(3), MaxLen(10)]
    value: float
    location: str
    timestamp: date
    district_id: int
    route_id: int
    sensor_id: int
    sensor_type: str


class SensorDataResponce(BaseModel):
    success: Boolean
    data: dict


class SSensorData(SensorDataBase):
    model_config = ConfigDict(from_attributes=True)
    data_id: int


class SSensorDataUpdate(SensorDataBase):
    model_config = ConfigDict(from_attributes=True)


class SensorDataCategoryQ:
    def __init__(self, category: str):
        self.category = category


class SensorDataLocationQ:
    def __init__(self, location: str):
        self.location = location


class SensorDataTypeCategoryQ:
    def __init__(self, sensor_type: str, category: str):
        self.sensor_type = sensor_type
        self.category = category
