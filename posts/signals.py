import os
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Post, Like, Comment, Notification
from accounts.models import UserProfile


@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
    if created:
        if instance.user != instance.post.user:
            Notification.objects.create(post=instance.post, user = instance.user, profile=instance.post.user, comment=instance, time_created=instance.time_created)



@receiver(post_save, sender=Like)
def like_notification(sender, instance, created, **kwargs):
    if created:
        if instance.user != instance.post.user:
            Notification.objects.create(post=instance.post, user=instance.user, profile=instance.post.user, liked=True, time_created=instance.time_created)
