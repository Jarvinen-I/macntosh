# -*- coding: utf-8 -*-

# /home/m/macntosh1/macntosh1.beget.tech/venv/lib/python3.8/site-packages/django/__init__.py

import os, sys
sys.path.insert(0, '/home/m/macntosh1/macntosh1.beget.tech/shop')
sys.path.insert(1, '/home/m/macntosh1/macntosh1.beget.tech/djangoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'macntosh1.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
