import os
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from cake_user.models.user_model import User
from tag.models.tag_model import Tag
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    updated = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post_tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to="media/", blank=True, null=True)

    def __str__(self):
        return f"{self.author}'s post in {self.post_tag}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


def content_file_name(instance, filename):
    return '/'.join(['media', instance.user.username, filename])


@receiver(models.signals.post_delete, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
