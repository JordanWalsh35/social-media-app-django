from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from . import models, forms
from accounts.models import UserProfile
from django.views import generic
from .post_functions import get_post
from django.http import HttpResponseRedirect


class CreatePostView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.CreatePostForm
    template_name = "posts/create_post.html"

    def get_success_url(self):
        return reverse("accounts:profile", args=[self.request.user.username])

    def form_valid(self, form):
        form.instance.user = UserProfile.objects.get(username=self.request.user)
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, generic.UpdateView):
    form_valid_message = "Your post has been updated."
    form_class = forms.UpdatePostForm
    template_name = "posts/create_post.html"

    def get(self, request, *args, **kwargs):
        post = models.Post.objects.get(pk=kwargs['pk'])

        if post.user != request.user:
            messages.warning(request, "You don't have permission to update this post.")
            return HttpResponseRedirect(reverse_lazy('posts:detailed', kwargs={'pk':kwargs['pk']}))
        else:
            return super().get(request, *args, **kwargs)


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = models.Post
    form_valid_message = "Your post has been deleted."
    success_url = reverse_lazy("home")
    template_name = 'posts/delete_post.html'

    def get(self, request, *args, **kwargs):
        post = models.Post.objects.get(pk=kwargs['pk'])

        if post.user != request.user:
            messages.warning(request, "You don't have permission to delete this post.")
            return HttpResponseRedirect(reverse_lazy('posts:detailed', kwargs={'pk':kwargs['pk']}))
        else:
            return super().get(request, *args, **kwargs)


class DetailedPostView(LoginRequiredMixin, generic.DetailView):
    model = models.Post
    context_object_name = 'post'
    template_name = "posts/detailed_post.html"
    queryset = models.Post.objects.all()


@login_required
def like_post_view(request, *args, **kwargs):
    try:
        post = Post.objects.get(pk=kwargs['pk'])
        _, created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            messages.warning(request, "You've already liked this post.")
    except Post.DoesNotExist:
        messages.warning(request, "Post does not exist.")
    return HttpResponseRedirect(reverse_lazy("posts:detailed", kwargs={"pk":kwargs["pk"]}))
