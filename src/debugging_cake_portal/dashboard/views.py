from django.shortcuts import render, redirect
from django.http import JsonResponse
from dashboard.models import Analysis
from comment.models import Comment
from posts.models.post_model import Post
from cake_user.models.user_model import User
from django.core import serializers
from django.contrib import messages
from django.views import View


def index(request):
    return render(request, 'index.html')


def pivot_data():
    dataset = Analysis.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


class Index(View):
    def get_context_data(self, request, **kwargs):
        user_count = User.objects.all().count()
        comment_count = Comment.objects.all().count()
        post_count = Post.objects.all().count()
        context = super().get_context_data(**kwargs)
        context.update({
            'user_count': user_count,
            'comment_count': comment_count,
            'post_count': post_count
        })

        return redirect(request, 'dashboard_with_pivot.html', context)
