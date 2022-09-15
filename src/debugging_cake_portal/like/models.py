from django.db import models
from cake_user.models.user_model import User
from posts.models.post_model import Post

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',max_length=10)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
