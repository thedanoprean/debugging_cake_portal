from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
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
from models.post_model import Post
from .serializers import PostSerializer
from .filters import PostFilter


@api_view(['POST'])
def adaugare_post(request):
    print(request.data)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Done", status=201, safe=False)
    else:
        return Response(serializer.errors, status=400)


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginated_filtered_posts = Paginator(self.filterset.qs, 2)
        page_number = self.request.GET.get('page')
        post_page_obj = paginated_filtered_posts.get_page(page_number)
        context.update({
            'filterset': self.filterset,
            'post_page_obj': post_page_obj
        })
        return context


# API REQUEST FACTORY

# Usage
class PostListView(FilteredListView):
    model = Post
    filterset_class = PostFilter
    paginate_by = 2
    template_name = 'index.html'
    ordering = ['-date_created']



# def show_all_posts_page(request):
#     context = {}
#
#     filtered_posts = PostFilter(
#         request.GET,
#         queryset=Post.objects.all()
#     )
#
#     # context['filtered_posts'] = filtered_posts.qs
#     context.update({
#         'filtered_posts': filtered_posts
#     })
#     return render(request, 'index.html', context=context)


# def list_posts(request):
#
#     # Intai filtrare, apoi paginare
#
#     posts = Post.objects.all().order_by('-date_created')
#     my_filter = PostFilter(request.GET, queryset=posts)
#     posts = my_filter.qs
#
#     p = Paginator(posts, 1)
#     page = request.GET.get('page')
#     posts = p.get_page(page)
#     nums = "a" * posts.paginator.num_pages
#
#     return render(request, 'index.html',
#                   {
#                       'posts': posts,
#                       'nums': nums,
#                       'my_filter': my_filter
#                   })

# post_list = Post.objects.all().order_by('-date_created')
#
# # Set up Pagination
# p = Paginator(post_list, 1)
# page = request.GET.get('page')
# posts = p.get_page(page)
# nums = "a" * posts.paginator.num_pages
#
# my_filter = PostFilter(request.GET, queryset=post_list)
# post_list = my_filter.qs
# return render(request, 'index.html',
#               {
#                   'posts': posts,
#                   'nums': nums,
#                   'my_filter': my_filter
#               })


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


def about_page(request):
    return render(request, 'about.html')


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


def onButtonClick(document=None):
    document.getElementById('textInput').className = "show"
