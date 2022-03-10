import os

from django.conf import settings

from DynamicDBUpdate.settings import load_plugin
from Main.models import Plugin
import zipfile


# mount plugins on system startup
def mountPlugins():
    plugins = Plugin.objects.all()
    for plugin in plugins:
        if plugin.active:
            print(load_plugin(str(os.path.basename(plugin.file.name)).split('.')[0]))


# Check if plugin already exists in the system
def checkPlugin(form):
    plugins = Plugin.objects.all()
    file = form.cleaned_data.get('file')
    with zipfile.ZipFile(file, 'r') as zip_ref:
        files = zip_ref.namelist()
        checkForTemplates(files)
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
