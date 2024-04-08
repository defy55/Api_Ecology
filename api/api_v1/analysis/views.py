from auth.dependencies_auth import get_current_active_user
from users.models import UserModel
from .models import Analyzes, Forecast
from fastapi import Query, Depends, Path, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from api_v1.dependencies import Dependencies

from api_v1.analysis.schemas import (
    SAnalysis,
)

router = APIRouter(tags=["ANALYSIS"])


@router.get("/")
async def get_all_analysis_data(
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[SAnalysis]:
    return await Dependencies.get_items(session=session, model=Analyzes)


@router.get("/forecast/")
async def get_all_forecasts(
    current_user: UserModel = Depends(get_current_active_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[SAnalysis]:
    return await Dependencies.get_items(session=session, model=Forecast)


# create
# update
# delete
# This functionality will be added when the data analysis system is in operation
