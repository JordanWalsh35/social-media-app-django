from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("photo", "caption")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("caption",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
