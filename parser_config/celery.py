import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parser_config.settings')

app = Celery('parser_config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
