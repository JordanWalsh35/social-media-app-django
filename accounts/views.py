from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from posts.models import Post

from . import forms
from .models import UserProfile


class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class MyLogoutView(LogoutView):
    next_page = "home"


class SignUpView(CreateView):
    form_class = forms.NewUserForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


@login_required
def user_profile_view(request, username):
    user = UserProfile.objects.get(username=username)
    posts = Post.objects.filter(user__username=user)
    active_user = request.user.username

    context={'username':username, 'user':user, 'posts':posts, 'active_user':active_user}

    if username != active_user:
        connected = user.followers.filter(user__username=active_user)
        context['connected'] = True if connected else False

    return render(request, 'accounts/profile.html', context)


class UpdateProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/update_account.html"


@login_required
def follow_view(request, username):
    user = UserProfile.objects.get(username=username)
    active_user = UserProfile.objects.get(user=request.user)

    try:
        user.followers.add(active_user)
        active_user.following.add(user)
    except Exception:
        messages.warning("System Error: Please Try Again")

    return HttpResponseRedirect(reverse_lazy("accounts:profile", kwargs={'username':user}))


@login_required
def unfollow_view(request, username):
    user = UserProfile.objects.get(username=username)
    active_user = UserProfile.objects.get(user=request.user)

    try:
        user.followers.remove(active_user)
        active_user.following.remove(user)
    except Exception:
        messages.warning("System Error: Please Try Again")

    return HttpResponseRedirect(reverse_lazy("accounts:profile", kwargs={'username':user}))
