from django import forms
from .models import stud

class Myregisterform(forms.ModelForm):
    class Meta:
        model=stud
        fields=["name","password","address","contact","email"]

