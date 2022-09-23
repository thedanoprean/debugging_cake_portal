import pytest

from django.urls import reverse, resolve

from src.debugging_cake_portal.posts.views import PostListView

 # 1) din os -> testam daca merge runserver

def test_posts_url_is_resolved(self):
    url = reverse('index')
    assert(resolve(url).func, PostListView)
