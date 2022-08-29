from topic.views.topic_views import TopicListView, TopicDetailView
from topic.views.rest import TopicRestView
from django.urls import path

app_name = "topic"

urlpatterns = [
    path('', TopicListView.as_view()),
    path('<int:pk>/', TopicDetailView.as_view()),

    # Django Rest Views
    path('rest/', TopicRestView.as_view()),
    path('rest/<int:pk>/', TopicRestView.as_view()),
]
