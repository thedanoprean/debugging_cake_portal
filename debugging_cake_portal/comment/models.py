from django.db import models
from posts.models import Post
from cake_user.models.user_model import User


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Comment by {self.user}'
