from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import UserProfile


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="posts")
    photo = models.ImageField(upload_to="post_photos", null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=100, blank=True)

    def __str__():
        return self.pk

    def get_absolute_url():
        return reverse("posts:detailed", kwargs={"username": self.user.username, "pk": self.pk})

    class Meta:
        ordering = ["-time_created"]
        verbose_name_plural = 'Posts'


# class Comment(models.Model):
#     user =  models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="commenter")


class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="like_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)
