import os

from django.shortcuts import render, redirect
from .signals import add_plugin
from DynamicDBUpdate.settings import load_plugin, unload_plugin
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


def allPlugins(request):
    data = {
        'plugins': Plugin.objects.all()
    }
    return render(request, 'allPlugins.html', data)


def toggleEnable(request, id):
    plugin = Plugin.objects.filter(id=id)
    if not plugin.count() > 0:
        return redirect('upload/')
    plugin = plugin.first()
    if request.POST:
        form = EnableForm(request.POST, instance=plugin)
        if form.is_valid():
            form.save()
            toggle = form.cleaned_data.get('active')
            if not toggle is None:
                if toggle:
                    load_plugin(str(os.path.basename(plugin.file.name)).split('.')[0])
                else:
                    print('to remove')
                    name = 'plugins.' + str(os.path.basename(plugin.file.name)).split('.')[0]
                    print(name)
                    arr = unload_plugin(str(os.path.basename(plugin.file.name)).split('.')[0])
                    print(arr)
                    print(arr[-1] == name)
                    print(arr.index(name))

    data = {
        'form': EnableForm(instance=plugin)
    }
    return render(request, 'enableForm.html', data)
