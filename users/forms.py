from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import EmailField
from .models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)

class UserLoginForm(AuthenticationForm):
    username = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
