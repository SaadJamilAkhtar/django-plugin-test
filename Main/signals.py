import django.dispatch
from django.dispatch import receiver

add_plugin = django.dispatch.Signal()


@receiver(add_plugin)
def out(sender, **kwargs):
    print("Here in this file")
