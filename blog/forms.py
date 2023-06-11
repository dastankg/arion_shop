from django import forms
from .models import Characteristic


class CharacteristicForm(forms.ModelForm):
    class Meta:
        model = Characteristic
        fields = ['name', 'value']
