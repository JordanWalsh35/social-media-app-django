from django.urls import path, include, re_path
from django.contrib import admin
from . import views

app_name = 'accounts'

urlpatterns = [
     path(r"signup/", views.SignUpView.as_view(), name="signup"),
     path(r"login/", views.MyLoginView.as_view(template_name="accounts/login.html"),name='login'),
     path(r"logout/", views.MyLogoutView.as_view(), name="logout"),
     path(r"<str:username>/", views.UserProfileView.as_view(), name="profile"),
]
