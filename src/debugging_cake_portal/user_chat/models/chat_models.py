from django.db import models
from cake_user.models.user_model import User
from .chatroom_models import ChatRoom


class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    room = models.ForeignKey(ChatRoom, null=True, on_delete=models.SET_NULL)
    test = models.CharField(max_length=100)