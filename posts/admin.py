from django.contrib import admin
from .models import Post, Like, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'time_created')
    list_filter = ('user', 'time_created')
    search_fields = ('user', 'post')
