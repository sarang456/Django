from django import forms
from .models import employee, Course, product, vehicle

class Emp_form(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'

class Course_form(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class product_form(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'

class vehicle_form(forms.ModelForm):
    class Meta:
        model = vehicle
        fields = '__all__'