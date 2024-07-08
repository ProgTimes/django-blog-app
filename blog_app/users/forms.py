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


class UserUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Bio'}), required=False)

    class Meta:
        model = User
        fields = ['avatar', 'email', 'username', 'bio']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email is already in use.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This username is already in use.')
        return username
