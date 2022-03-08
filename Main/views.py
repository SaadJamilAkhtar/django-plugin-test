import os

from django.shortcuts import render
from .signals import add_plugin
from DynamicDBUpdate.settings import load_plugin
from .forms import *
import zipfile


def index(request):
    if request.POST:
        data = load_plugin("Plugin")
        return render(request, 'index.html', {"data": data})
    return render(request, 'index.html')


def upload(request):
    if request.POST:
        form = PluginForm(request.POST, request.FILES)
        if form.is_valid():
            plugin = form.save()
            with zipfile.ZipFile(plugin.file, 'r') as zip_ref:
                zip_ref.extractall('plugins/')
                load_plugin(str(os.path.basename(plugin.file.name)).split('.')[0])
    form = PluginForm()
    return render(request, 'upload.html', {'form': form})


def mountPlugins():
    plugins = Plugin.objects.all()
    for plugin in plugins:
        if plugin.active:
            load_plugin(str(os.path.basename(plugin.file.name)).split('.')[0])
