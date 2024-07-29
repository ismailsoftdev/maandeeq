"""
WSGI config for maandeeq project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from maandeeq.settings.base import DEBUG

from django.core.wsgi import get_wsgi_application

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maandeeq.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maandeeq.settings.prod')

application = get_wsgi_application()
