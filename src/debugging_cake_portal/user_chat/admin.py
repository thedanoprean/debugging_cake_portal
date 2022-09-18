from django.contrib import admin
from .models.chat_models import Chat
from .models.chatroom_models import ChatRoom


admin.site.register(Chat)
admin.site.register(ChatRoom)

