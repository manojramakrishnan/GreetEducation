from django import forms
from django.contrib.auth.models import User
from . import models

class AdminSignupForm(forms.ModelForm):
    class Meta:
        model= User
        fields =['first_name','last_name','username','password']

class TeacherSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields =['first_name','last_name','username','password']

class StudentSignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields =['first_name','last_name','username','password']
