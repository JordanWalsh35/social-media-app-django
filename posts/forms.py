from django import forms
from .models import Post, Comment, AbuseReport


class CreatePostForm(forms.ModelForm):
    photo = forms.FileField(label="", widget = forms.ClearableFileInput(attrs={'class':'upload-file'}))
    caption = forms.CharField(label="", widget = forms.Textarea(attrs={'class':'caption-input', 'placeholder':'Caption'}))

    class Meta:
        model = Post
        fields = ("photo", "caption")



class UpdatePostForm(forms.ModelForm):
    caption = forms.CharField(label="", widget = forms.Textarea(attrs={'class':'caption-input', 'placeholder':'Caption'}))

    class Meta:
        model = Post
        fields = ("caption",)



class CreateCommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'comment-box', 'placeholder':'Add a comment...'}))

    class Meta:
        model = Comment
        fields = ("comment",)



class ReportForm(forms.ModelForm):
    report = forms.CharField(label="", widget = forms.TextInput(attrs={'class':'caption-input', 'placeholder':'Write a complaint about this post...'}))

    class Meta:
        model = AbuseReport
        fields = ("report",)
