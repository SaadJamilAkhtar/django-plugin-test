from django import forms
from .models import *


class PluginForm(forms.ModelForm):
    class Meta:
        model = Plugin
        fields = ['file']
        exclude = ['filename']


class EnableForm(forms.ModelForm):
    class Meta:
        model = Plugin
        fields = ['active']
