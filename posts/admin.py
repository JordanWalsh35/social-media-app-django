from django.contrib import admin
from .models import Post, Like, Comment, Notification, AbuseReport

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(AbuseReport)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'time_created')
    list_filter = ('user', 'time_created')
    search_fields = ('user', 'post')
