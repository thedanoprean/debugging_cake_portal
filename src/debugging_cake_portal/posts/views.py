from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from comment.form import CommentForm
from comment.models import Comment
from cake_user.models.user_model import User
from .models import Post
from .serializers import PostSerializer
from django.contrib import messages


@api_view(['POST'])
def adaugare_post(request):
    print(request.data)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Done", status=201, safe=False)
    else:
        return Response(serializer.errors, status=400)


class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects
    serializer = PostSerializer

    def list(self, request):
        posts = self.queryset.all()
        serializer = self.serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer(post)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({'success': 'Team deleted successfully'}, status.HTTP_200_OK)


def homepage(request):
    return render(request, 'index.html')


def list_posts(request):
    posts = Post.objects.all()
    data = {
        'posts': posts
    }
    return render(request, 'index.html', data)

    # TODO: implement about.html


def about_page(request):
    return render(request, 'about.html')


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_created']


class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("post-detail", kwargs={'pk': int(post.id)}))

    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        user_count = User.objects.all().count()
        comment_count = Comment.objects.all().count()
        post_count = Post.objects.all().count()
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
            'user_count': user_count,
            'comment_count': comment_count,
            'post_count': post_count
        })

        return context


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'post_tag', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.request.FILES
        form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'post_tag', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.request.FILES
        if form.is_valid():
            return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def count_posts_of(user):
    return Post.objects.filter(author=user).count()


def num_post(request):
    num_posts = Post.objects.filter(author=request.user).count()
    return render(request, 'some_template.html', {'num_posts': num_posts})


def onButtonClick(document=None):
    document.getElementById('textInput').className = "show"
