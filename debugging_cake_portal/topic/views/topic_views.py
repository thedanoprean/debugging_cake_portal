from django.views.generic import ListView, DetailView
from topic.models.topic_model import Topic


class TopicListView(ListView):
    model = Topic
    context_object_name = 'topic_list'
    template_name = "topic_list_template.html"


class TopicDetailView(DetailView):
    model = Topic
    context_object_name = 'topic_report'
    template_name = "topic_detail_template.html"
