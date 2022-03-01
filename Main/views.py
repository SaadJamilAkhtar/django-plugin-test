from django.shortcuts import render
from .signals import add_plugin
from DynamicDBUpdate.settings import load_plugin
from .forms import *


def index(request):
    if request.POST:
        data = load_plugin("Plugin")
        return render(request, 'index.html', {"data": data})
    return render(request, 'index.html')


def upload(request):
    if request.POST:
        form = PluginForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = PluginForm()
    return render(request, 'upload.html', {'form': form})
