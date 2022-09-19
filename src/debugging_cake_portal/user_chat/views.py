from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Chat, ChatRoom
from django.views import View


class ChatIndex(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'chat/chat_index.html')


class ChatRoomView(LoginRequiredMixin, View):
    def get(self, request, room_name):
        room = ChatRoom.objects.filter(name=room_name).first()
        chats = []

        if room:
            chats = Chat.objects.filter(room=room)
            chats.save()
        else:
            room = ChatRoom(name=room_name)
            room.save()

        return render(request, 'chat/chat_room.html', {
            'room_name': room_name,
            'chats': chats
        })
