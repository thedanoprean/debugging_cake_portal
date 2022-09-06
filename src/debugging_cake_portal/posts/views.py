from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from rest_framework import viewsets, status, views
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser

from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, JsonResponse
from .serializers import PostSerializer
from .forms import UploadPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView


# class FileUploadView(views.APIView):
#     parser_classes = (FileUploadParser,)
#
#     def put(self, request, filename, format=None):
#         form = PostSerializer(request.POST, request.FILES)
#         file_obj = request.FILES['file']
#         if file_obj.is_valid():
#             file_obj.save()
#             return Response(status=204)
#         else:
#             form = PostSerializer()
#         return render(request, 'CreatePost.html', {'form': form})
from comment.form import CommentForm
from comment.models import Comment


def upload_file(request):
    if request.method == 'POST':
        form = PostSerializer(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = PostSerializer()
    return render(request, 'CreatePost.html', {'form': form})


def Upload_Form(request):
    if request.method == 'POST':
        form = UploadPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/view/')
    else:
        form = UploadPost()
    return render(request, 'CreatePost.html', {'form': form})


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

    # def create(self, request):
    #     serializer = self.serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response({'error': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)

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
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })

        return context


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'post_tag', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'post_tag', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
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

# def delete(request, pk):
#     if request.method == 'GET':
#         post = Post.objects.get(pk=pk)
#         if post:
#             post.delete()
#     return redirect('posts/')
