#!/usr/bin/python3
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MASKWEB.settings")

application = get_wsgi_application()
