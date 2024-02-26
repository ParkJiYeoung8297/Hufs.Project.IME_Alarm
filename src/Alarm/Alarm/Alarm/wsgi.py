"""
WSGI config for Alarm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from .tasks import scheduler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Alarm.settings")

application = get_wsgi_application()

# 스케줄링 작업 실행
scheduler.start()