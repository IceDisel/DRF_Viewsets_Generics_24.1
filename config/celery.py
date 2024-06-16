from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     from users.tasks import deactivate_inactive_users
#
#     # Вызов задачи каждые сутки
#     sender.add_periodic_task(
#         crontab(hour=0, minute=0),
#         deactivate_inactive_users.s(),
#     )
