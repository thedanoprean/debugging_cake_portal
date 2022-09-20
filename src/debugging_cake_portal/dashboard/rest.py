from rest_framework import status
from comment.models import Comment
from posts.models.post_model import Post
from cake_user.models.user_model import User
from dashboard.models import Analysis
from dashboard.serializer.analysis_serializer import AnalysisSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class DashboardRestView(APIView):
    serializer_class = AnalysisSerializer

    def post(self, request):
        serializer = AnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_context_data(self, **kwargs):
        user_count = User.objects.all().count()
        comment_count = Comment.objects.all().count()
        post_count = Post.objects.all().count()
        context = super().get_context_data(**kwargs)
        context.update({
            'user_count': user_count,
            'comment_count': comment_count,
            'post_count': post_count
        })

        return context
