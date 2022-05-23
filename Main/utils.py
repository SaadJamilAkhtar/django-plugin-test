import os

from django.conf import settings

from DynamicDBUpdate.settings import load_plugin
from Main.models import Plugin
import zipfile


# mount plugins on system startup
def mountPlugins():
    try:
        plugins = Plugin.objects.all()
        for plugin in plugins:
            if plugin.active:
                print(load_plugin(str(os.path.basename(plugin.file.name)).split('.')[0]))
    except:
        pass


# Check if plugin already exists in the system
def checkPlugin(form):
    plugins = Plugin.objects.all()
    file = form.cleaned_data.get('file')
    with zipfile.ZipFile(file, 'r') as zip_ref:
        files = zip_ref.namelist()
        if not checkConfig(files):
            return False
        for plugin in plugins:
            if str(files[0]).strip() == str(plugin.filename).strip():
                return False
        return True


def checkForTemplates(files):
    for name in files:
        sec = name.split("/")
        if len(sec) > 1:
            sec = sec[1].strip()
            if sec == "templates":
                return True
    return False


def loadTemplates(plugin):
    base_dir_path = f'{settings.PLUGIN_DIRECTORY}/{plugin.filename}/templates/{plugin.filename}/'
    os.makedirs(f'templates/{plugin.filename}')
    for file in os.listdir(base_dir_path):
        os.rename(base_dir_path + str(file), f"templates/{plugin.filename}/{str(file)}")


# Check if config file exists in plugin
def checkConfig(files):
    for name in files:
        if "config.json" in name:
            return True
    return False


# Check if plugin require python deps
def checkPythonDeps(data):
    if len(data['python deps']) > 0:
        return True
    return False


def installPythonDeps(data):
    if checkPythonDeps(data):
        for dep in data['python deps']:
            os.system(f"pip install {dep}")
