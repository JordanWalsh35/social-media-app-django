from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(auth.models.User):
    profile_picture = models.ImageField(upload_to="accounts/profile_pics", blank=True, null=True)

    def __str__(self):
        return self.username


# class Connection(models.Model):
#     follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="follower")
#     following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="following")
#     time_created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return "{} : {}".format(self.follower.username, self.following.username)
