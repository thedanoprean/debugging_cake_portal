from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
        'label': 'Comment'
    }))

    class Meta:
        model = Comment
        fields = ('content',)
