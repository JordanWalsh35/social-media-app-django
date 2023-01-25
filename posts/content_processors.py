from django.db.models import Count, Q
from .models import Notification, Post

def notification_count(request):
    if request.user.is_authenticated:
        notification_count = Notification.objects.filter(
        Q(profile=request.user) &
        Q(read_status='Unread')).count()
    else:
        notification_count = None
    return {'notification_count' : notification_count}
