from django.urls import path

from .views import chatrooms_view, room_view

urlpatterns = [
    path('chatrooms/', chatrooms_view, name='chatrooms'),
    path('<slug:slug>/', room_view, name='room'),
]