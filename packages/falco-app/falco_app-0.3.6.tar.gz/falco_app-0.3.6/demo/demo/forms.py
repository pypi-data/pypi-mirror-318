
from django import forms

from .models import Something


class SomethingForm(forms.ModelForm):
    class Meta:
        model = Something
        fields = ('id', 'name', 'description') 


