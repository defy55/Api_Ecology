from contextlib import asynccontextmanager

from fastapi import FastAPI, Query, Depends, Path
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from fastapi_cache.decorator import cache
from fastapi.middleware.cors import CORSMiddleware

from tasks.tasks import celery
from api_v1 import router as include_router
from users.views import router as users_router
from users.views import router as users_router

from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(
        "redis://redis:6379/0", encoding="utf8", decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(include_router, prefix=settings.api_v1_prefix)
app.include_router(users_router, prefix=settings.api_v1_prefix)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)


def CREATE_JOB():
    task = celery.send_task("tasks.sched_test", args=[], kwargs={})
