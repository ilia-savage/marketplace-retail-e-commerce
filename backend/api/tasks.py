from celery import shared_task
from .services import VisitDataBaseService

@shared_task
def save_visits():
    """
    Сохранение посещений пользователей из кеша в базу
    """
    service = VisitDataBaseService()
    service.save_to_db()