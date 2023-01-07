from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path(r"create/", views.CreatePostView.as_view(), name="create"),
    # path(r"(?P<pk>\d+)/$", views.DetailedPostView.as_view(), name="detailed")
]
