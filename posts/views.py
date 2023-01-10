from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from .forms import CreatePostForm, UpdatePostForm
from.models import Post, Like, Comment
from django.contrib import messages
from accounts.models import UserProfile
from django.views import generic
from django.http import HttpResponseRedirect


class CreatePostView(LoginRequiredMixin, generic.CreateView):
    form_class = CreatePostForm
    template_name = "posts/create_post.html"

    def get_success_url(self):
        return reverse("accounts:profile", args=[self.request.user.username])

    def form_valid(self, form):
        form.instance.user = UserProfile.objects.get(username=self.request.user)
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, generic.UpdateView):
    form_valid_message = "Your post has been updated."
    form_class = UpdatePostForm
    template_name = "posts/create_post.html"

    def get(self, request, *args, **kwargs):
        post = models.Post.objects.get(pk=kwargs['pk'])

        if post.user != request.user:
            messages.warning(request, "You don't have permission to update this post.")
            return HttpResponseRedirect(reverse_lazy('posts:detailed', kwargs={'pk':kwargs['pk']}))
        else:
            return super().get(request, *args, **kwargs)


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    form_valid_message = "Your post has been deleted."
    success_url = reverse_lazy("home")
    template_name = 'posts/delete_post.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])

        if post.user != request.user:
            messages.warning(request, "You don't have permission to delete this post.")
            return HttpResponseRedirect(reverse_lazy('posts:detailed', kwargs={'pk':kwargs['pk']}))
        else:
            return super().get(request, *args, **kwargs)


class DetailedPostView(LoginRequiredMixin, generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "posts/detailed_post.html"
    queryset = Post.objects.all()


@login_required
def like_post_view(request, *args, **kwargs):
    post = Post.objects.get(pk=kwargs['pk'])
    user = UserProfile.objects.get(user=request.user)
    like = Like(user=user, post=post)
    return HttpResponseRedirect(reverse_lazy("posts:detailed", kwargs={'pk':kwargs['pk']}))


def unlike_post_view(request, *args, **kwargs):
    # try:
    user = UserProfile.objects.get(user=request.user)
    post = Post.objects.get(pk=kwargs['pk'])
    like = Like.objects.get(pk=kwargs['pk'], user=user)
    # except Like.DoesNotExist:
    #     messages.warning(request, "You didn't like the post.")
    # else:
    like.delete()

    return HttpResponseRedirect(reverse_lazy("posts:detailed", kwargs={'pk':kwargs['pk']}))


def add_comment_view(request, *args, **kwargs):
    return HttpResponseRedirect(reverse_lazy("posts:detailed", kwargs={'pk':kwargs['pk']}))


def delete_comment_view(request, *args, **kwargs):
    return HttpResponseRedirect(reverse_lazy("posts:detailed", kwargs={'pk':kwargs['pk']}))
