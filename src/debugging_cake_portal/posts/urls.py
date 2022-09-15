from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework import views
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    homepage,
    adaugare_post,
    # Upload_Form,
    PostListView,
    PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView, list_posts
)

urlpatterns = [
    path('posts/', login_required(list_posts), name='index'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create_post/', PostCreateView.as_view(), name='create-post'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
router = DefaultRouter(trailing_slash=True)
router.register(r'posts', PostViewSet)

urlpatterns.extend(router.urls)
