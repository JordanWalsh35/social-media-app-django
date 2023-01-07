from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

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


class UserProfileView(LoginRequiredMixin, DetailView):

    template_name = "accounts/profile.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = UserProfile.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['username']
        context['username'] = username

        return context
