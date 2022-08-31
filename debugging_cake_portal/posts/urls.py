from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework import views
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    homepage,
    list_posts,
    adaugare_post,
    Upload_Form,
    PostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    path('posts/', login_required(PostListView.as_view()), name='index'),
    path('view/posts/', list_posts, name='index'),
    path('view/posts/<int:pk>/', PostDetailView.as_view(), name='index'),
    path('create_post/', PostCreateView.as_view(), name='create-post'),
    path('add_post/', adaugare_post),
]
router = DefaultRouter(trailing_slash=True)
router.register(r'posts', PostViewSet)

urlpatterns.extend(router.urls)
