from django.db import models


class Plugin(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='plugins/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
