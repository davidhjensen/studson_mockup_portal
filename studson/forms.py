# forms.py
from django import forms
from .models import Mockup

class MockupForm(forms.ModelForm):
    class Meta:
        model = Mockup
        fields = ['company_name', 'helmet_color', 'helmet_model', 'size', 'front_logo', 'back_logo', 'left_logo', 'right_logo']
