from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
from accounts import views as account_views
from posts import views as post_views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("feed/", post_views.feed_post_view, name="feed"),
    path("new-user/", views.new_user_view, name="new-user"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("search/", account_views.user_search, name="search"),
    path("notifications/", views.view_notifications, name="notifications"),
    path("notification-read/<int:pk>/", views.notification_status, name="status"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
