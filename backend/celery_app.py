import os
import time

from celery import Celery
from celery.schedules import crontab
from celery import Celery
from django.conf import settings

def get_custom_schedule():
    return crontab(minute="*/1")


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

custom_schedule = get_custom_schedule()

app.conf.beat_schedule = {
    'save_visits_periodically': {
        'task': 'api.tasks.save_visits', 
        'schedule': custom_schedule,  
    }
}

@app.task()
def debug_task():
    time.sleep(5)
    print('Hello from debug task')