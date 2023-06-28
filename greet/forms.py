from django import forms
from django.contrib.auth.models import User
from . import models

class AdminSignupForm(forms.ModelForm):
    class Meta:
        model= User
        fields =['first_name','last_name','username','password']

class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields =['first_name','last_name','username','password']
class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra
        fields= ['salary','mobile','status']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields =['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields =['roll','cl','mobile','fee','status']