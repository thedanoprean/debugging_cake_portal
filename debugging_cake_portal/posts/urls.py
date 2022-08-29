from django.contrib import admin
from django.urls import path
from rest_framework import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, homepage, list_posts, adaugare_post, Upload_Form

urlpatterns = [
    path('view/', homepage, name='index'),
    path('view/posts/', list_posts, name='index'),
    path('view/create_post/', Upload_Form, name='index'),
    path('add_post/', adaugare_post),
]
router = DefaultRouter(trailing_slash=True)
router.register(r'posts', PostViewSet)

urlpatterns.extend(router.urls)
