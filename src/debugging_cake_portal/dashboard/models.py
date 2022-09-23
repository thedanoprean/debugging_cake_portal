from django.core.validators import MinValueValidator
from django.db import models
from comment.models import Comment
from posts.models.post_model import Post
from cake_user.models.user_model import User, Role
from dashboard.validators.dashboard_validator import *


class Analysis(models.Model):
    nr_users = models.CharField(max_length=50, default=User.objects.count(), null=True, validators=[validate_nr_users, MinValueValidator(0)])
    nr_comments = models.CharField(max_length=50, default=Comment.objects.count(), null=True, validators=[validate_nr_comments, MinValueValidator(0)])
    nr_posts = models.CharField(max_length=50, default=Post.objects.count(), null=True, validators=[validate_nr_posts, MinValueValidator(0)])
    nr_roles = models.CharField(max_length=50, default=Role.objects.count(), null=True, validators=[validate_nr_roles, MinValueValidator(0)])
    # type_roles = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL, validators=[validate_roles])

    created = models.DateTimeField(auto_now_add=True)

    # these fields must be in Post module
    # nr_likes = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    # nr_views = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)

    # class Meta:
    #     analysis = ('-created successfully',)

    def __str__(self):
        return 'Analysis from: {}, {}, {}, {}'.format(self.nr_users, self.nr_comments, self.nr_posts, self.nr_roles)
