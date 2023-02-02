from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from .models import UserProfile


class LoginForm(AuthenticationForm):
    username = UsernameField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Username'}))
    password = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'input-boxes', 'placeholder':'Password'}),)


class NewUserForm(UserCreationForm):
    email = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Email'}))
    username = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Username'}))
    password1 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'class':'input-boxes', 'placeholder':'Password'}),)
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'input-boxes', 'placeholder':'Confirm Password'}), strip=False,)

    class Meta:
        model = UserProfile
        fields = ("email", "username" , "password1", "password2",)


class UpdateAccountForm(forms.ModelForm):
    username = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Username'}))
    first_name = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'First name'}))
    last_name = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Last name'}))
    bio = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Bio'}))
    email = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Email'}))
    profile_picture = forms.FileField(label="", widget = forms.ClearableFileInput(attrs={'class':'update-profiler'}))

    class Meta:
        fields =  ("username", "first_name", "last_name", "email", "bio", "profile_picture",)
        model = UserProfile
