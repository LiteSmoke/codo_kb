# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1593565/data/www/gtingo.com/codo_kb')
sys.path.insert(1, '/var/www/u1593565/data/www/gtingo.com/codo_kb_env/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'codo_kb.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()