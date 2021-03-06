"""DynamicDBUpdate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.dispatch import receiver
from django.urls import path, include
from Main.views import *
from .settings import plugin_loaded, plugin_unloaded
from Main.utils import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('upload', upload, name='add'),
    path('all/', allPlugins),
    path('plugin/<int:id>', toggleEnable, name='toggle'),
    path('migrate', runMigrations)
]


@receiver(plugin_loaded)
def load_urls(sender, **kwargs):
    try:
        urlpatterns.append(path(str(sender).lower() + "/", include('plugins.' + str(sender) + ".urls"), name=sender))
    except:
        pass


@receiver(plugin_unloaded)
def unload_urls(sender, **kwargs):
    for url in urlpatterns:
        if str(url.pattern).strip() == (str(sender).lower() + "/"):
            urlpatterns.remove(url)


mountPlugins()
