from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import UserProfile
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="posts")
    photo = models.ImageField(upload_to="post_photos", null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("posts:detailed", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-time_created"]
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    user =  models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="commenter")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    comment = models.TextField(max_length=200)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)

    class Meta:
        ordering = ['time_created']


class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="like_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str('{} : {}'.format(self.user.username, self.post.pk))

    class Meta:
        unique_together = ("post", "user")


class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name="sender")
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name="receiver")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    liked = models.BooleanField(default=False, null=True)
    followed = models.BooleanField(default=False, null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True)

    options=(("Unread", "Unread"),
             ("Read", "Read"),)

    read_status = models.CharField(max_length=10, choices=options, default="Unread")


class AbuseReport(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name="reporter")
    report = models.TextField(max_length=300, blank=False)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
