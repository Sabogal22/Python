from socket import fromshare
from django import forms
from .models import Motos

class MotosForm(forms.ModelForm):
    class Meta:
        model = Motos
        fields = '__all__'