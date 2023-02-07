from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse

from .forms import CreatePostForm, UpdatePostForm, CreateCommentForm, ReportForm
from .models import Post, Like, Comment
from accounts.models import UserProfile



class CreatePostView(LoginRequiredMixin, generic.CreateView):
    form_class = CreatePostForm
    template_name = "posts/create_post.html"

    def get_success_url(self):
        return reverse("accounts:profile", args=[self.request.user.username])

    def form_valid(self, form):
        form.instance.user = UserProfile.objects.get(username=self.request.user)
        return super().form_valid(form)



class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'posts/delete_post.html'

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        return super().get(request, *args, **kwargs)



class ReportAbuseView(LoginRequiredMixin, generic.CreateView):
    form_class = ReportForm
    template_name = "posts/report_post.html"

    def get_success_url(self):
        return reverse("home")

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs.get('pk'))
        form.instance.user = UserProfile.objects.get(username=self.request.user)
        form.save()
        return super().form_valid(form)


@login_required
def update_post_view(request, **kwargs):
    post = Post.objects.get(pk=kwargs['pk'])

    if request.method == 'POST':
        edit_form = UpdatePostForm(data=request.POST, instance=post)
        if edit_form.is_valid():
            edit_form.save()
        return HttpResponseRedirect(reverse_lazy("posts:detailed", kwargs={'pk':kwargs['pk']}))
    else:
        edit_form = UpdatePostForm()

    context = {'edit_form':edit_form}
    return render(request, "posts/edit_post.html", context)



@login_required
def detailed_post_view(request, pk):
    user = UserProfile.objects.get(user=request.user)
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    new_comment = None

    try:
        like = Like.objects.get(post=post, user=user)
        liked = True
    except:
        liked = False

    if request.method == 'POST':
        comment_form = CreateCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = user
            new_comment.save()
        return HttpResponseRedirect(reverse_lazy("posts:detailed", kwargs={'pk':pk}))
    else:
        comment_form = CreateCommentForm()

    context = {'post':post, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form, 'liked':liked}

    return render(request, "posts/detailed_post.html", context)



@login_required
def feed_post_view(request):
    profile = UserProfile.objects.get(user=request.user)
    username = profile.username
    following = profile.following.all()
    posts = Post.objects.filter(user__in=following)
    new_comment = None

    for post in posts:
        post.liked = Like.objects.filter(user=profile, post=post).exists()
        post.comments = Comment.objects.filter(post=post)
        post.comment_form = CreateCommentForm()

    if request.method == 'POST':
        post_id = request.GET.get('post_id')
        post = Post.objects.get(id=post_id)
        post.comment_form = CreateCommentForm(data=request.POST)
        if post.comment_form.is_valid():
            new_comment = post.comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = profile
            new_comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {'posts':posts}

    return render(request, "feed.html", context)



def like_unlike_view(request, **kwargs):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        user = UserProfile.objects.get(user=request.user)

        if Like.objects.filter(user=user, post=post).exists():
            like = Like.objects.get(post=post, user=user)
            like.delete()
            value = 'unlike'
        else:
            like = Like(user=user, post=post)
            like.save()
            value = 'like'

        data = {'like_count':post.liked_post.count(), 'value':value}

        return JsonResponse(data, safe=False)
    return redirect("feed")



def post_likes(request, pk):
    user = UserProfile.objects.get(user=request.user)
    post = Post.objects.get(pk=pk)
    likes = Like.objects.filter(post=post)

    context = {'post':post, 'likes':likes, 'user':user}
    return render(request, "posts/post_likes.html", context)
