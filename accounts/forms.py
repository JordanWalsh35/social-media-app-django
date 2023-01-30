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



class UpdateAccountForm(forms.ModelForm): #UserChangeForm
    username = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Username'}))
    first_name = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'First name'}))
    last_name = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'input-boxes', 'placeholder':'Last name'}))
    # password1 = forms.CharField(label="", strip=False, widget=forms.PasswordInput(attrs={'class':'input-boxes', 'placeholder':'Password'}),)
    # profile_picture = forms.ImageField(label="", widget = forms.ClearableFileInput(attrs={'class':'upload-file'}))


    class Meta:
        fields =  ("username", "first_name", "last_name", "email", "bio", "profile_picture",)
        model = UserProfile



# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ["bio"]


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
