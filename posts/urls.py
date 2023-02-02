from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("create/", views.CreatePostView.as_view(), name="create"),
    path("<int:pk>/detailed/", views.detailed_post_view, name="detailed"),
    path("<int:pk>/edit", views.update_post_view, name="edit"),
    path("<int:pk>/delete", views.DeletePostView.as_view(), name="delete"),
    path("<int:pk>/like/", views.like_unlike_view, name="like"),
    path("<int:pk>/report/", views.ReportAbuseView.as_view(), name="report"),
    path("<int:pk>/likes/", views.post_likes, name="likes"),
]
