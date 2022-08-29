from django.db import models
from django.contrib.auth import get_user_model

from tag.models.tag_model import Tag
from posts.models import Post
from topic.validators.topic_validators import validate_title

User = get_user_model()


class Topic(models.Model):
    title = models.CharField(max_length=100, validators=[validate_title])
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
