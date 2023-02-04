from django.contrib import admin
from .models import Post, Like, Comment, Notification, AbuseReport


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'time_created')
    list_filter = ('user', 'post', 'time_created')
    search_fields = ('user', 'post')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'time_created', 'caption')
    list_filter = ('user', 'time_created')
    search_fields = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'comment', 'time_created')
    list_filter = ('user', 'post', 'time_created')
    search_fields = ('user', 'post')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile', 'post', 'comment', 'liked', 'followed', 'time_created')
    list_filter = ('user', 'profile', 'post', 'time_created')
    search_fields = ('user', 'post')


@admin.register(AbuseReport)
class AbuseAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'report', 'time_created')
    list_filter = ('user', 'post', 'time_created')
    search_fields = ('user', 'post')
