from django.urls import path, include, re_path
from django.contrib import admin
from . import views

app_name = 'accounts'

urlpatterns = [
     path("signup/", views.SignUpView.as_view(), name="signup"),
     path("login/", views.MyLoginView.as_view(template_name="accounts/login.html"),name='login'),
     path("logout/", views.MyLogoutView.as_view(), name="logout"),
     path("<str:username>/", views.UserProfileView.as_view(), name="profile"),
]
