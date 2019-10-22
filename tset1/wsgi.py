"""
WSGI config for tset1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tset1.settings')
#
# application = get_wsgi_application()

import os
import sys
from os.path import join,dirname,abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))

sys.path.insert(0, PROJECT_DIR)
sys.path.append('/home/xyaw/web_pay_v35/xvenv/Lib/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'web_pay_v35.settings'

application = get_wsgi_application()
