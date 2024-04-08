from celery import Celery
import os, sys
import sys
import time
from core.config import settings

sys.path.append(os.getcwd())

celery = Celery("tasks", broker=settings.CELERY_BROKER_URL)


@celery.task(name="tasks.tester")
def test(data):
    time.sleep(1)
    return "ok"
