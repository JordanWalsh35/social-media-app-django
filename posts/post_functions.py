from django.db.models import Prefetch
from .models import Post, Like
from accounts.models import UserProfile


def get_post(pk=None):
    if not pk:
        return None
    post = Post.objects.select_related('user').prefetch_related(Prefetch('liked_post', queryset=Like.objects.select_related('user'), to_attr='like_user')).get(pk=pk)
    # post = Post.objects.get(pk=pk)
    post.like_user = [like_user.user for users in post.like_user]
    return post


# def get_posts(user=None, wall=False):
#     if not user:
#         return None
#     if isinstance(user, str):
#         user = UserProfile.objects.get(username=user)
#     if not user.is_authenticated:
#         return None
#
#     users = [user, ]
#
#     if wall:
#         users += Connection.objects.filter(follower__username=user).values_list('following', flat=True)
#     posts = Post.objects.select_related('user').prefetch_related(Prefetch('liked_post', queryset=Like.objects.select_related('user'), to_attr='like_user')).filter(user__in=users).order_by('-time_created')
#
#     for post in posts:
#         post.like_user = [like_user.user for user in post.like_user]
#
#     return posts
