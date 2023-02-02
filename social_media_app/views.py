from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from posts.models import Notification, Post
from accounts.models import UserProfile



def home_view(request):
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        following = user.following.count()
        if following == 0:
            return HttpResponseRedirect(reverse("new-user"))
        return HttpResponseRedirect(reverse("feed"))
    return HttpResponseRedirect(reverse("accounts:login"))



def new_user_view(request):
    new_user = UserProfile.objects.get(user=request.user)
    all_users = UserProfile.objects.all()

    context = {'new_user':new_user, 'all_users':all_users}
    return render(request, "accounts/new_user.html", context)



def view_notifications(request):
    if request.user.is_authenticated:
        view_notifications = Notification.objects.filter(profile=request.user)
        context = {'view_notifications' : view_notifications}
        return render(request, "notifications.html", context)
    return HttpResponseRedirect(reverse("accounts:login"))



def notification_status(request, *args, **kwargs):
    username = UserProfile.objects.get(username=request.user.username)
    object_notification = Notification.objects.get(pk=kwargs['pk'])

    object_notification.read_status = 'Read'
    object_notification.save()

    if object_notification.followed:
        return HttpResponseRedirect(reverse_lazy('accounts:followers', kwargs={'username' : username}))
    else:
        post_pk = object_notification.post.pk
    return HttpResponseRedirect(reverse_lazy('posts:detailed', kwargs={'pk' : post_pk}))
