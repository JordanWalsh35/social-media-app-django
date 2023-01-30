from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    photo = forms.FileField(label="", widget = forms.ClearableFileInput(attrs={'class':'upload-file'}))
    caption = forms.CharField(label="", widget = forms.Textarea(attrs={'class':'caption-input', 'placeholder':'Caption'}))

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
    comment = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'comment-box', 'placeholder':'Add a comment...'}))

    class Meta:
        model = Comment
        fields = ("comment",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
