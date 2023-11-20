from django import forms
from home.models import Telefon


class AddAuto(forms.ModelForm):
    class Meta:
        model = Telefon
        fields = ['nomi', 'rangi', 'narxi']


class EditAuto(forms.ModelForm):
    class Meta:
        model = Telefon
        fields = ['nomi', 'rangi', 'narxi']
