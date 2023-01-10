from django.urls import path, include, re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'accounts'

urlpatterns = [
     path("signup/", views.SignUpView.as_view(), name="signup"),
     path("login/", views.MyLoginView.as_view(template_name="accounts/login.html"),name='login'),
     path("logout/", views.MyLogoutView.as_view(), name="logout"),
     path("<str:username>/", views.user_profile_view, name="profile"),
     path("<str:username>/update/", views.UpdateProfileView.as_view(), name="update"),
     path("<str:username>/follow/", views.follow_view, name="follow"),
     path("<str:username>/unfollow/", views.unfollow_view, name="unfollow"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
