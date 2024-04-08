from typing import Any, Annotated
from auth.dependencies_auth import get_current_active_user
from users.models import UserModel
from fastapi import Query, Depends, Path, APIRouter, status
from api_v1.routes.models import District, Route
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from api_v1.dependencies import Dependencies

from api_v1.routes.schemas import (
    DistrictsInfo,
    DistrictsInfoCreate,
    DistrictsInfoUpdate,
    RouteInfo,
    RouteInfoUpdate,
)

router = APIRouter(tags=["DISTRICTS"])


@router.get("/", response_model=list[DistrictsInfo])
async def get_districts(
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await Dependencies.get_items(session=session, model=District)


@router.get("/routes/", response_model=list[RouteInfo])
async def get_routes(
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await Dependencies.get_items(session=session, model=Route)


@router.get("/{district_number}/", response_model=DistrictsInfo)
async def get_district_to_id(
    district_number: int,
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    dict_params = {
        "model": District,
        "name_param": District.district_number,
        "value": district_number,
    }
    return await Dependencies.get_item_to_param(session=session, **dict_params)


@router.post(
    "/add_district/",
    response_model=DistrictsInfoCreate,
    status_code=status.HTTP_201_CREATED,
)
async def add_district(
    sensor_data_in: DistrictsInfoCreate,
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> DistrictsInfoCreate:
    dict_params = {
        "model": District,
        "value": sensor_data_in,
    }
    return await Dependencies.create_item(session=session, **dict_params)


@router.post(
    "/add_route/",
    response_model=RouteInfo,
    status_code=status.HTTP_201_CREATED,
)
async def add_route(
    sensor_data_in: RouteInfo,
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> RouteInfo:
    dict_params = {
        "model": Route,
        "value": sensor_data_in,
    }
    return await Dependencies.create_item(session=session, **dict_params)


@router.patch("/update_district/{sensor_id}/")
async def update_district(
    district_update: DistrictsInfoUpdate,
    district_number: Annotated[int, Path],
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> DistrictsInfoUpdate:
    dict_params = {
        "model": District,
        "item_id": district_number,
        "update": district_update,
        "name_param": District.district_number,
    }
    return await Dependencies.update_item(session=session, **dict_params)


@router.patch("/update_route/{sensor_id}/")
async def update_route(
    route_update: RouteInfoUpdate,
    route_number: Annotated[int, Path],
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> RouteInfoUpdate:
    dict_params = {
        "model": Route,
        "item_id": route_number,
        "update": route_update,
        "name_param": Route.route_number,
    }
    return await Dependencies.update_item(session=session, **dict_params)


@router.delete("/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def district_delete(
    district_number: Annotated[int, Path],
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    dict_params = {
        "model": District,
        "item_id": district_number,
        "name_param": District.district_number,
    }
    await Dependencies.item_delete(session=session, **dict_params)


@router.delete("/route/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def district_delete(
    route_number: Annotated[int, Path],
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    dict_params = {
        "model": Route,
        "item_id": route_number,
        "name_param": Route.route_number,
    }
    await Dependencies.item_delete(session=session, **dict_params)
