# admin_app/forms.py
from django import forms
from .models import Plants

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = ['Name', 'price']
