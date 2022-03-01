from django import forms
from .models import *


class PluginForm(forms.ModelForm):
    class Meta:
        model = Plugin
        fields = '__all__'
