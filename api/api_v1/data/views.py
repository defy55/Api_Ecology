from sys import prefix
from typing import Annotated
from auth.dependencies_auth import get_current_active_user
from users.models import UserModel
from core.models import db_helper
from api_v1.dependencies import Dependencies
from .models import SensorData
from fastapi import Query, Depends, Path, APIRouter


from api_v1.data.schemas import (
    SSensorData,
    SSensorDataUpdate,
)
from fastapi import Query, Depends, Path, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=["DATA"])


@router.get("/")
async def get_all_sensors_data(
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[SSensorData]:
    return await Dependencies.get_items(session=session, model=SensorData)


@router.post(
    "/create_data/",
    response_model=SSensorData,
    status_code=status.HTTP_201_CREATED,
)
async def create_data(
    data_in: SSensorData,
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[SSensorData]:
    dict_params = {
        "model": SensorData,
        "value": data_in,
    }
    return await Dependencies.create_item(session=session, **dict_params)


@router.patch("/static/{data_id}/")
async def update_static_sensor_data(
    sensor_update: SSensorDataUpdate,
    data_id: Annotated[int, Path],
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> SSensorData:
    dict_params = {
        "model": SensorData,
        "item_id": data_id,
        "update": sensor_update,
        "name_param": SensorData.data_id,
    }
    return await Dependencies.update_item(session=session, **dict_params)


@router.delete("/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def data_delete(
    data_id: Annotated[int, Path],
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    dict_params = {
        "model": SensorData,
        "item_id": data_id,
        "name_param": SensorData.data_id,
    }
    await Dependencies.item_delete(session=session, **dict_params)
