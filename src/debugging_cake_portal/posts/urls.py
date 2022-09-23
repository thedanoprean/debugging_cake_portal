from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    PostListView,
    PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='index'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create_post/', PostCreateView.as_view(), name='create-post'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('posts/', FilterView.as_view(model=Post), name="list-posts"),
]
router = DefaultRouter(trailing_slash=True)
router.register(r'posts', PostViewSet)

urlpatterns.extend(router.urls)
