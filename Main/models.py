from django.db import models
from django.conf import settings


class Plugin(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=f'{settings.PLUGIN_DIRECTORY}/')
    active = models.BooleanField(default=True)
    filename = models.CharField(max_length=255, default="")
    author = models.CharField(max_length=255)
    version = models.FloatField(default=1.0)
    entry = models.CharField(max_length=255)

    def getEntryPoint(self):
        return self.filename + self.entry

    def __str__(self):
        return self.name
