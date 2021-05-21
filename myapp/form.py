from django import forms
from .models import Employee, Project

class EmployeeForm(forms.ModelForm):
    email = forms.EmailField(min_length=5, max_length=10, widget=forms.TextInput())
    class Meta:
        model = Employee
        fields = '__all__' #['name', 'city']
        error_messages = {
            'name': {'required':'Name is required'},
            'city': {'required': 'City is not Required'}
        }
        widgets = {'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Enter name Here'}),
                   'city': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Enter City Here'}),
                   'email': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Enter Email Here'})}

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        error_messages = {
            'name': {'required': 'Project Name is required '},
            'type': {'required': 'Project Type is required'}
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Enter prject Name'}),
            'type': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Enter Project Type'}),
        }

