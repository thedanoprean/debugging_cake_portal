from django.db import models
from comment.models import Comment
from posts.models.post_model import Post
from cake_user.models.user_model import User


class Analysis(models.Model):
    # nr_users = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # nr_comments = models.ForeignKey(Comment, null=True, on_delete=models.SET_NULL, related_name='number_comments')
    nr_users = models.CharField(max_length=50, default=User.objects.count(), null=True)
    nr_comments = models.CharField(max_length=50, default=Comment.objects.count(), null=True)
    nr_posts = models.CharField(max_length=50, default=Post.objects.count(), null=True)

    created = models.DateTimeField(auto_now_add=True)

    # these fields must be in Post module
    # nr_likes = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    # nr_views = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)

    # class Meta:
    #     analysis = ('-created successfully',)

    def __str__(self):
        return 'Analysis from: {}, {}, {}'.format(self.nr_users, self.nr_comments, self.nr_posts)
