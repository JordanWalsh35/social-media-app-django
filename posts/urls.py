from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("create/", views.CreatePostView.as_view(), name="create"),
    path("<int:pk>/", views.detailed_post_view, name="detailed"),
    path("<int:pk>/update", views.UpdatePostView.as_view(), name="update"),
    path("<int:pk>/delete", views.DeletePostView.as_view(), name="delete"),
    path("<int:pk>/like/", views.like_post_view, name="like"),
    path("<int:pk>/unlike/", views.unlike_post_view, name="unlike"),
]
