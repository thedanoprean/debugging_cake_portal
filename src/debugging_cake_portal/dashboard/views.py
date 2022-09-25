from django.shortcuts import render, redirect
from django.http import JsonResponse
from dashboard.models import Analysis
from comment.models import Comment
from dashboard.serializer.analysis_serializer import OrderSerializer
from posts.models.post_model import Post
from cake_user.models.user_model import User, Role
from django.core import serializers
from django.http import HttpResponseForbidden
import json


def index(request):
    return render(request, 'index.html')


def pivot_data(request):

    if not hasattr(request, 'user') or not request.user.is_superuser:
        return HttpResponseForbidden()

    dataset = [
        ['Fields', 'users', 'posts', 'comments'],
        ['moderator', User.objects.filter(roles__id=3).count(), Post.objects.filter(author__roles=3).count(),
         Comment.objects.filter(user__roles=3).count()],
        ['compo', User.objects.filter(roles__id=2).count(), Post.objects.filter(author__roles=2).count(),
         Comment.objects.filter(user__roles=2).count()],
        ['developer', User.objects.filter(roles__id=1).count(), Post.objects.filter(author__roles=1).count(),
         Comment.objects.filter(user__roles=1).count()]
    ]

    print(dataset)
    return JsonResponse(dataset, safe=False)


def dashboard_with_pivot(request):

    if not hasattr(request, 'user') or not request.user.is_superuser:
        return HttpResponseForbidden()

    user_count = User.objects.all().count()
    comment_count = Comment.objects.all().count()
    post_count = Post.objects.all().count()
    role_count = Role.objects.all().count()

    data_dict = {
        'nr_users': User.objects.count(),
        'nr_comments': Comment.objects.count(),
        'nr_posts': Post.objects.count(),
        'nr_roles': Role.objects.count()
    }

    serializer = OrderSerializer(data=data_dict)
    serializer.update(instance=Analysis.objects.get(pk=1), validated_data=data_dict)

    return render(request, 'dashboard_with_pivot.html', {
        'user_count': user_count,
        'comment_count': comment_count,
        'post_count': post_count,
        'role_count': role_count,
    })
