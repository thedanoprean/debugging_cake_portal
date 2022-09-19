from django.db import models
from cake_user.models.user_model import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Chatroom {self.name}"


class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.content}"
