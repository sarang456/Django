from django import forms
from .models import service

class Service_form(forms.ModelForm):
    class Meta:
        model = service
        fields = '__all__'
