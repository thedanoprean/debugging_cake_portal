import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView
from comment.form import CommentForm
from comment.models import Comment
from like.models import Like
from notifications.models import Notification
from .models import Post


def like_unlike_post(request):
    ok = True
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        if not created:
            if not like.value:
                like.value = True
            else:
                like.value = False
        else:
            like.value = False
        post_obj.save()
        like.save()
        if not like.value:
            notify = Notification(post=like.post, sender=like.user, user=like.post.author, notification_type=1)
            notifications = Notification.objects.filter(sender=like.user).order_by('-date')
            for noti in notifications:
                if noti.post == notify.post and noti.user == notify.user:
                    notify = Notification.objects.get(post=noti.post, sender=noti.sender)
                    notify.date = datetime.datetime.now()
                    notify.is_seen = False
            notify.save()
        # else:
        #     if like.value:
        #         notify = Notification.objects.get(post=like.post, sender=like.user, user=like.post.author)
        #         print(like.post)
        #         print(like.user)
        #         print(like.post.author)
        #         notify.delete()

    return redirect('index')


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
