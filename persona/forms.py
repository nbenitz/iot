from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
    	model = get_user_model()
    	fields = ["username", "email", "password1", "password2"]

class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')