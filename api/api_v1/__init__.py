from fastapi import APIRouter

from .sensors.views import router as sensors_router
from .data.views import router as data_router
from .routes.views import router as routes_router
from .analysis.views import router as analysis_router

from .auth_jwt.jwt_auth import router as jwt_auth_router

from api_v1.sensors.models import *
from api_v1.routes.models import *
from api_v1.data.models import *
from api_v1.analysis.models import *

router = APIRouter()
router.include_router(router=sensors_router, prefix="/sensors")
router.include_router(router=routes_router, prefix="/districts")
router.include_router(router=data_router, prefix="/data")
router.include_router(router=analysis_router, prefix="/analysis")
router.include_router(router=jwt_auth_router, prefix="/jwt")
