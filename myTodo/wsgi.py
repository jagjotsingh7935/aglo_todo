"""
WSGI config for myTodo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

if not os.path.exists('/tmp/db.sqlite3'):
    call_command('migrate')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myTodo.settings')

application = get_wsgi_application()

app = application