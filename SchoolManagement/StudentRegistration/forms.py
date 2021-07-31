from django.contrib.auth.models import User
from django import forms
from .models import Student



class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']