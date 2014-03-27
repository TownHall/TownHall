__author__ = 'daniel'
from django import forms
from models import Pitch

class PitchForm(forms.ModelForm):
    class Meta:
        model = Pitch
        fields = ['title', 'text']