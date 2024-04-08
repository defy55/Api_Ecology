from typing import Annotated

from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordRequestForm
from exception.exceptions import Invalidauthenticated
from users.models import UserModel

from api_v1.sensors.models import StationarySensor
from core.models import db_helper

from auth.dependencies_auth import get_current_active_user
from fastapi import (
    Depends,
    Path,
    APIRouter,
    Request,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.dependencies import Dependencies
from api_v1.sensors.schemas import (
    SensorCreateStatic,
    SensorInfo,
    SensorInfoStatic,
    SensorInfoStaticUpdate,
)

router = APIRouter(tags=["SENSORS"])
security = HTTPBasic()


@router.get("/static/", response_model=list[SensorInfoStatic])
async def get_statics_sensors(
    request: Request,
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    if request.cookies.get("refresh_token") == None:
        raise Invalidauthenticated
    return await Dependencies.get_items(session=session, model=StationarySensor)


@router.get("/static/{sens_id}/", response_model=SensorInfo)
async def get_sensor_static_id(
    sensor_id: int,
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    dict_params = {
        "model": StationarySensor,
        "name_param": StationarySensor.sensor_id,
        "value": sensor_id,
    }
    return await Dependencies.get_item_to_param(session=session, **dict_params)


@router.post(
    "/create_static_sensor/",
    response_model=SensorCreateStatic,
    status_code=status.HTTP_201_CREATED,
)
async def create_sensor_static(
    sensor_data_in: SensorCreateStatic,
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> SensorCreateStatic:
    dict_params = {
        "model": StationarySensor,
        "value": sensor_data_in,
    }
    return await Dependencies.create_item(session=session, **dict_params)


@router.patch("/static/{sensor_id}/")
async def update_static_sensor_data(
    sensor_update: SensorInfoStaticUpdate,
    sensor_id: Annotated[int, Path],
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> SensorInfoStatic:
    dict_params = {
        "model": StationarySensor,
        "item_id": sensor_id,
        "update": sensor_update,
        "name_param": StationarySensor.sensor_id,
    }
    return await Dependencies.update_item(session=session, **dict_params)


@router.delete("/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def sensor_delete(
    sensor_id: Annotated[int, Path],
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    dict_params = {
        "model": StationarySensor,
        "item_id": sensor_id,
        "name_param": StationarySensor.sensor_id,
    }
    await Dependencies.item_delete(session=session, **dict_params)
