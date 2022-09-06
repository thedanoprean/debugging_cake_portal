from django import forms
from .models import Post


class UploadPost(forms.ModelForm):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    file = forms.FileField()

    class Meta:
        model = Post
        fields = ("title", "description", "author", "post_tag", "file",)
