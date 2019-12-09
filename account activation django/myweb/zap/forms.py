from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')
    first_name=forms.CharField(max_length=30, help_text='Required')
    last_name=forms.CharField(max_length=30, help_text='Required')
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

