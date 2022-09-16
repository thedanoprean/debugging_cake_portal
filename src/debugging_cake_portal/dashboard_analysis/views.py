from django.shortcuts import render, redirect
from django.http import JsonResponse
from dashboard_analysis.models import Analysis
from comment.models import Comment
from posts.models.post_model import Post
from cake_user.models.user_model import User
from django.core import serializers
from django.contrib import messages


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Analysis.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def analysis(request):
    # Get Counts
    user_count = User.objects.all().count()
    comment_count = Comment.objects.all().count()
    reply_count = Comment.objects.all().count()

    post_list = Post.objects.all().order_by('-date_created')

    if request.user.is_superuser:
        if request.method == "POST":
            # Get list of checked box id's
            id_list = request.POST.getlist('boxes')

            # Uncheck all posts
            post_list.update(approved=False)

            # Update the database
            for x in id_list:
                Post.objects.filter(pk=int(x)).update(approved=True)

            # Show success message and redirect
            messages.success(request, "Post list has been updated!")
            return redirect('list-posts')

        else:
            return render(request, 'dashboard_with_pivot.html',
                          {"user_count": user_count,
                           "comment_count": comment_count,
                           "reply_count": reply_count
                           })

    else:
        messages.success(request, "You aren't authorized to view this page!")
        return redirect('admin')

    return render(request, 'dashboard_with_pivot.html')
