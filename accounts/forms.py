from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from .models import UserProfile


class NewUserForm(UserCreationForm):
    email = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Email'}))
    username = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Username'}))
    password1 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'class':'input-boxes', 'placeholder':'Password'}),)
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'input-boxes', 'placeholder':'Confirm Password'}), strip=False,)

    class Meta:
        model = UserProfile
        fields = ("email", "username" , "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UpdateAccountForm(UserChangeForm):
    class Meta:
        fields = '__all__'
        model = UserProfile

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
