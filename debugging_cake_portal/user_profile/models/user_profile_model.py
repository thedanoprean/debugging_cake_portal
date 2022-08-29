from django.db import models
from cake_user.models.user_model import User
from posts.models.post_model import Post
from tag.models.tag_model import Tag


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    _full_name = models.CharField(max_length=100, blank=True, null=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    about_me = models.TextField(max_length=140, blank=True, null=False)
    posts = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    tags = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user.username} Profile'
