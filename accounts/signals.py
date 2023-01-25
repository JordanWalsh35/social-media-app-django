import os
from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from posts.models import Notification
from .models import UserProfile


@receiver(m2m_changed, sender=UserProfile.followers.through)
def follow_notification(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        Notification.objects.create(user=instance.followers.last(), profile=instance, followed=True)
