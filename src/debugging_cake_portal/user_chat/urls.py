from django.urls import path

from views import ChatIndex, ChatRoomView

urlpatterns = [
    path('', ChatIndex.as_view(), name='chat_index'),
    path('<str:room_name>/', ChatRoomView.as_view(), name='chat_room')
]
