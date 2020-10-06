from django import forms  
from .models import Employee  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):  
    firstName = forms.CharField(label="First name",max_length=50)  
    lastName  = forms.CharField(label="Last name", max_length = 100)
    employeeId= forms.CharField(label="ID ",max_length=50)  
    city  = forms.CharField(label="City", max_length = 100)    
    class Meta:  
            model = Employee  
            fields = ("firstName","lastName","employeeId","city") 

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )