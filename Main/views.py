from django.shortcuts import render
from .signals import add_plugin
from DynamicDBUpdate.settings import load_plugin


def index(request):
    if request.POST:
        data = load_plugin("Plugin")
        return render(request, 'index.html', {"data": data})
    return render(request, 'index.html')
