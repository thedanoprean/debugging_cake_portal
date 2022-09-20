from django.shortcuts import render
from like.models import Like
from notifications.models import Notification
from django.db.models.signals import post_save
import datetime


def listLike(request):
    likes = Like.objects.all
    data = {
        'likes': likes
    }
    return render(request, 'index.html', data)


# def user_liked_post(instance, *args, **kwargs):
#     notify = Notification(post=instance.post, sender=instance.user, user=instance.post.author, notification_type=1)
#     notifications = Notification.objects.filter(user=instance.user).order_by('-date')
#     if instance.value:
#         for noti in notifications:
#             if noti.post == notify.post and noti.user == notify.user:
#                 notify = Notification.objects.get(post=noti.post, sender=noti.user)
#                 notify.date = datetime.datetime.now()
#         notify.save()
#
#
# like = Like()
# post_save.connect(like.user_liked_post, sender=Like)
