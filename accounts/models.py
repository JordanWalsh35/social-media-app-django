from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(auth.models.User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    profile_picture = models.ImageField(upload_to="profile_pics")
    bio = models.CharField(max_length=300, blank=True)
    following = models.ManyToManyField("UserProfile", related_name="user_following", blank=True)
    followers = models.ManyToManyField("UserProfile", related_name="user_followers", blank=True)

    def __str__(self):
        return self.username
