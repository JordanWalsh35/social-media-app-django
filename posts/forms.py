from django import forms
from . import models

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ("photo", "caption")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ("caption",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
