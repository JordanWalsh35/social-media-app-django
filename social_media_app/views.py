from django.views import generic
from posts.models import Post
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse



class HomeView(generic.ListView):
    model = Post
    template_name = 'feed.html'
    context_object_name = 'posts'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse("accounts:login"))

    # def get_queryset(self):
    #     return get_posts(self.request.user, wall=True)
