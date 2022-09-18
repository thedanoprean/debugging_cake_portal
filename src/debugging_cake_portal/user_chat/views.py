from django.shortcuts import render
from .models.chatroom_models import ChatRoom
from .models.chat_models import Chat


def chat_index(request):
    return render(request, 'chat/chat_index.html', {})


def chat_room(request, room_name):
    room = ChatRoom.objects.filter(name=room_name).first()
    chats = []

    chats = Chat.objects.filter(room=room)

    return render(request, 'chat/chat_room.html', {
        'room_name': room_name
        })
