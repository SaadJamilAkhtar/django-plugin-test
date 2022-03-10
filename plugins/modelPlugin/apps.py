import os

from django.apps import AppConfig


class ModelpluginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plugins.modelPlugin'

    def ready(self):
        print('plugin ready')
        os.system('python manage.py migrate')
