from __future__ import absolute_import, unicode_literals

# Это позволит импортировать celery при запуске Django
from .celery import app as celery_app

__all__ = ('celery_app',)
