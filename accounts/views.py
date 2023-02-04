from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from posts.models import Post, Like, Comment
from .forms import LoginForm, NewUserForm, UpdateAccountForm
from posts.forms import CreateCommentForm
from .models import UserProfile



class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    form_class = LoginForm



class MyLogoutView(LogoutView):
    next_page = "home"



class SignUpView(CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"



class FollowersView(LoginRequiredMixin, ListView):
    template_name = "accounts/followers.html"
    model = UserProfile
    context_object_name ='user'

    def get_queryset(self):
        obj = get_object_or_404(UserProfile, username = self.kwargs.get('username'))
        return obj



class FollowingView(LoginRequiredMixin, ListView):
    template_name = "accounts/following.html"
    model = UserProfile
    context_object_name ='user'

    def get_queryset(self):
        obj = get_object_or_404(UserProfile, username = self.kwargs.get('username'))
        return obj



@login_required
def user_profile_view(request, username):
    user = UserProfile.objects.get(username=username)
    posts = Post.objects.filter(user__username=user)
    active_user = request.user.username
    profile = UserProfile.objects.get(user=request.user)

    context={'username':username, 'user':user, 'posts':posts, 'active_user':active_user}

    if username != active_user:
        connected = user.followers.filter(user__username=active_user)
        context['connected'] = True if connected else False

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

    return render(request, 'accounts/profile.html', context)



@login_required
def update_profile_view(request, username):
    user = UserProfile.objects.get(username=username)

    if request.method == 'POST':
        user_form = UpdateAccountForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid():
            user_form.save()
            new_username = request.POST['username']
            return HttpResponseRedirect(reverse_lazy("accounts:profile", kwargs={'username':new_username}))
    else:
        user_form = UpdateAccountForm(instance=request.user)

    context = {'user_form':user_form}

    return render(request, "accounts/update_account.html", context)



@login_required
def follow_view(request, username):
    user = UserProfile.objects.get(username=username)
    active_user = UserProfile.objects.get(user=request.user)

    try:
        user.followers.add(active_user)
        active_user.following.add(user)
    except Exception:
        messages.warning("System Error: Please Try Again")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required
def unfollow_view(request, username):
    user = UserProfile.objects.get(username=username)
    active_user = UserProfile.objects.get(user=request.user)

    try:
        user.followers.remove(active_user)
        active_user.following.remove(user)
    except Exception:
        messages.warning("System Error: Please Try Again")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def user_search(request):
    search = request.GET.get('search')
    payload = []
    if search:
        objs = UserProfile.objects.filter(username__icontains = search)

        for obj in objs:
            payload.append(obj.username)

    return JsonResponse({
        'status' : True,
        'data' : payload
    })
