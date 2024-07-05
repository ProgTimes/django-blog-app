from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}), label="")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label="")

    class Meta:
        model = User
        fields = ('username', 'password')
