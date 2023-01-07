from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path(r"", views.HomeView.as_view(), name="home"),
    path(r"admin/", admin.site.urls),
    path(r"accounts/", include("accounts.urls", namespace="accounts")),
    path(r"posts/", include("posts.urls", namespace="posts")),
]
