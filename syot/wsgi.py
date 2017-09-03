"""
WSGI config for syot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/syot-project/syot')
sys.path.append('/home/ubuntu/syot-project/env/lib/python3.6')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "syot.settings")

application = get_wsgi_application()
