from django.urls import path

from .views import chatrooms, room

urlpatterns = [
    path('chatrooms/', chatrooms, name='chatrooms'),
    path('<slug:slug>/', room, name='room'),
]