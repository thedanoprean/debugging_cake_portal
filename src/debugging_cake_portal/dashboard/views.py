from django.shortcuts import render, redirect
from django.http import JsonResponse
from dashboard.models import Analysis
from comment.models import Comment
from dashboard.serializer.analysis_serializer import OrderSerializer
from posts.models.post_model import Post
from cake_user.models.user_model import User, Role
from django.core import serializers


def index(request):
    return render(request, 'index.html')


def pivot_data(self):
    dataset = Analysis.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def dashboard_with_pivot(request):
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
