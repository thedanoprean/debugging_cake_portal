from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cake_user.models.user_model import User
from .models import ChatRoom, Message


@login_required()
def chatrooms_view(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chats/chatrooms.html', {
        "rooms": rooms
    })


@login_required
def room_view(request, slug):
    room = ChatRoom.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    return render(request, 'chats/room.html', {'room': room, 'messages': messages})
