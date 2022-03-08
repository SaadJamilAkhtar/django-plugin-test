from django.db import models
from django.conf import settings


class Plugin(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=f'{settings.PLUGIN_DIRECTORY}/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
