from django import forms
from .models import *


class PluginForm(forms.ModelForm):
    class Meta:
        model = Plugin
        fields = '__all__'
        exclude = ['filename']


class EnableForm(forms.ModelForm):
    class Meta:
        model = Plugin
        fields = ['active']
