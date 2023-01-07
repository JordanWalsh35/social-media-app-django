from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("create/", views.CreatePostView.as_view(), name="create"),
    path("<int:pk>/", views.DetailedPostView.as_view(), name="detailed")
]
