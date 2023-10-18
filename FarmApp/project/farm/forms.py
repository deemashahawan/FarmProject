from django import forms
from .models import Animal, AnimalType,Feed,Employee

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'type', 'gender', 'feeds', 'weight']

class AnimalTypeForm(forms.ModelForm):
    class Meta:
        model = AnimalType
        fields = ['name']

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['name', 'amount']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position']      