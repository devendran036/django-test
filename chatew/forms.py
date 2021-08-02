from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CreateUserForm(UserCreationForm):
    class Meta:
        models=User
        fields=['username','email','password1','password2','image']
    
